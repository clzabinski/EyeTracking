"""
Demonstration of the GazeTracking library.
Check the README.md for complete documentation.
"""
import sys
import os
from OutlierDetection import DetectOutlier
from flask import request
from math import floor
from MathLib import calc_accuracy, calc_accuracy_avg, calc_precision
import cv2
from keyboard import is_pressed
from gaze_tracking import GazeTracking
#import imutils
from DataLib import take_point
import ScreenResolution

screenrez = ScreenResolution.get_screen_resolution()


def main():
    test_senario = True
    header_printed = False
    test_points = [
        (320, 180),
        (640, 180),
        (960, 180),
        (1280, 180),
        (1600, 180),
        (320, 360),
        (640, 360),
        (960, 360),
        (1280, 360),
        (1600, 360),
        (320, 540),
        (640, 540),
        (960, 540),
        (1280, 540),
        (1600, 540),
        (360, 720),
        (640, 720),
        (960, 720),
        (1280, 720),
        (1600, 720),
        (360, 900),
        (640, 900),
        (960, 900),
        (1280, 900),
        (1600, 900),
    ]

    test_index = 0
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
                    #middle_point = (floor(1920 * horiz_ratio), floor(1080 * vert_ratio))
                    middle_point = ((floor((left_pupil[0] + right_pupil[0])) * horiz_ratio),floor((left_pupil[1] + right_pupil[1]) * vert_ratio))
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
                            # data={"x": middle_point[0], "y": middle_point[1]},
                            data={"x": middle_x, "y": middle_y},
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
        cv2.putText(frame, "Ratios: " + str(horiz_ratio) + " " + str(vert_ratio),
            (90, 235),
            cv2.FONT_HERSHEY_DUPLEX,
            0.9,
            (147, 58, 31),
            1,)

        cv2.imshow("Demo", frame)
        dist_to_screen = 64
        if is_pressed(" "):
            number_of_datapoints = 21
            if header_printed == False:
                take_point("BEGINING", "TEST", "HERE")
                header_printed = True

        if number_of_datapoints > 0:
            list_of_points.append(take_point(left_pupil, right_pupil, middle_point))
            number_of_datapoints -= 1
            if number_of_datapoints == 0 and test_senario == False:
                accuracy = calc_accuracy(list_of_points, (690, 210), dist_to_screen)
                avg_accuracy = calc_accuracy_avg(accuracy)
                precision = calc_precision(list_of_points, (690, 210), dist_to_screen)

                print("accuracy avg = " + str(avg_accuracy))
                print("accuracy =  " + str(accuracy))
                print("precision = " + str(precision))
                take_point("=====", "=====", "=====")
                list_of_points = []

            try:
                if number_of_datapoints == 0 and test_senario:
                    accuracy = calc_accuracy(
                        list_of_points, test_points[test_index], dist_to_screen
                    )
                    avg_accuracy = calc_accuracy_avg(accuracy)
                    precision = calc_precision(
                        list_of_points, test_points[test_index], dist_to_screen
                    )

                    print(
                        "accuracy avg for point "
                        + str(test_index + 1)
                        + ":"
                        + str(avg_accuracy)
                    )
                    print(
                        "accuracy for point "
                        + str(test_index + 1)
                        + ":"
                        + str(accuracy)
                    )
                    print(
                        "precision for point "
                        + str(test_index + 1)
                        + ":"
                        + str(precision)
                    )
                    take_point("Accuarcy Avg", str(avg_accuracy), "N/A")
                    take_point("Accuarcy", str(accuracy), "N/A")
                    take_point("Precision", str(precision), "N/A")
                    take_point("=====", "=====", "=====")

                    test_index += 1
                    list_of_points = []

                    if test_index > 24:
                        test_senario = False
                        take_point("END", "TEST", "HERE")
            except:
                take_point("N/A", "N/A", "N/A")

        if cv2.waitKey(1) == 27:
            break

    webcam.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
