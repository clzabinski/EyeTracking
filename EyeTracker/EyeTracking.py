"""
Demonstration of the GazeTracking library.
Check the README.md for complete documentation.
"""
import sys
import os
from OutlierDetection import DetectOutlier
from flask import request
import requests
from math import floor
from MathLib import calc_accuracy, calc_accuracy_avg, calc_precision
import cv2
from keyboard import is_pressed
from gaze_tracking import GazeTracking
import imutils
from DataLib import take_point
import ScreenResolution

screenrez = ScreenResolution.get_screen_resolution()


def main():
    gaze = GazeTracking()
    webcam = cv2.VideoCapture(0)
    webcam.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    webcam.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

    take_info = True

    number_of_datapoints = 0
    list_of_points = []
    middle_arr_1 = []
    middle_arr_2 = []
    sample_count = 60
    while True:
        # We get a new frame from the webcam
        _, frame = webcam.read()
        frame = cv2.flip(frame, 1)
        # imutils.resize(frame, width=1920, height=1080)
        # We send this frame to GazeTracking to analyze it
        gaze.refresh(frame)
        frame = gaze.annotated_frame()
        # frame = cv2.resize(frame, (1920, 1080), interpolation=cv2.INTER_AREA)
        text = ""

        if gaze.is_blinking():
            text = "Blinking"
        elif gaze.is_right():
            text = "Looking right"
        elif gaze.is_left():
            text = "Looking left"
        elif gaze.is_center():
            text = "Looking center"

        cv2.putText(
            frame, text, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2
        )

        left_pupil = gaze.pupil_left_coords()
        right_pupil = gaze.pupil_right_coords()
        middle_point = None

        try:
            if left_pupil and right_pupil:
                if gaze.horizontal_ratio():
                    horiz_ratio = gaze.horizontal_ratio()
                    vert_ratio = gaze.vertical_ratio()
                    middle_point = (floor(1280 * horiz_ratio), floor(720 * vert_ratio))
                    middle_arr_1.append(middle_point[0])
                    middle_arr_2.append(middle_point[1])

                    
                    if len(middle_arr_1) == sample_count:
                        middle_x, middle_y = DetectOutlier(middle_arr_1, middle_arr_2)
                        cv2.line(
                            frame,
                            (int(middle_x) - 5, int(middle_y)),
                            (int(middle_x) + 5, int(middle_y)),
                            (0, 0, 255),
                        )
                        cv2.line(
                            frame,
                            (int(middle_x), int(middle_y) - 5),
                            (int(middle_x), int(middle_y) + 5),
                            (0, 0, 255),
                        )
                        middle_arr_1 = []
                        middle_arr_2 = []
                        requests.post(
                            "http://127.0.0.1:5000/coordinates",
                            #data={"x": middle_point[0], "y": middle_point[1]},
                            data={"x":middle_x, "y": middle_y}
                        )
        except:
            pass
        cv2.putText(
            frame,
            "Left pupil:  " + str(left_pupil),
            (90, 130),
            cv2.FONT_HERSHEY_DUPLEX,
            0.9,
            (147, 58, 31),
            1,
        )
        cv2.putText(
            frame,
            "Right pupil: " + str(right_pupil),
            (90, 165),
            cv2.FONT_HERSHEY_DUPLEX,
            0.9,
            (147, 58, 31),
            1,
        )
        cv2.putText(
            frame,
            "Middle point: " + str(middle_point),
            (90, 200),
            cv2.FONT_HERSHEY_DUPLEX,
            0.9,
            (147, 58, 31),
            1,
        )

        cv2.imshow("Demo", frame)

        if is_pressed(" "):
            number_of_datapoints = 21

        if number_of_datapoints > 0:
            list_of_points.append(take_point(left_pupil, right_pupil, middle_point))
            number_of_datapoints -= 1
            if number_of_datapoints == 0:
                accuracy = calc_accuracy(list_of_points, (690, 210), 60)
                avg_accuracy = calc_accuracy_avg(accuracy)
                precision = calc_precision(list_of_points, (690, 210), 60)

                print("accuracy avg = " + str(avg_accuracy))
                print("accuracy =  " + str(accuracy))
                print("precision = " + str(precision))
                list_of_points = []

        if cv2.waitKey(1) == 27:
            break

    webcam.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
