"""
Demonstration of the GazeTracking library.
Check the README.md for complete documentation.
"""

from math import floor
from MathLib import calc_accuracy, calc_accuracy_avg, calc_precision
import cv2
from keyboard import is_pressed
from gaze_tracking import GazeTracking
from DataLib import take_point
from ..API.app import pass_coordinates
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
    while True:
        # We get a new frame from the webcam
        _, frame = webcam.read()
        # imutils.resize(frame, width=1920, height=1080)
        # We send this frame to GazeTracking to analyze it
        gaze.refresh(frame)

        frame = gaze.annotated_frame()
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
        middle_pupil = None

        if left_pupil and right_pupil:
            middle_pupil = (floor((left_pupil[0] + right_pupil[0]) / 2), floor((left_pupil[1] + right_pupil[1]) / 2))
            pass_coordinates(middle_pupil)
            x_mid, y_mid = middle_pupil
            cv2.line(frame, (int(x_mid) - 5, int(y_mid)), (int(x_mid) + 5, int(y_mid)), (0,0,255))
            cv2.line(frame, (int(x_mid), int(y_mid) - 5), (int(x_mid), int(y_mid) + 5), (0,0,255))

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
            "Nose Bridge: " + str(middle_pupil),
            (90, 200),
            cv2.FONT_HERSHEY_DUPLEX,
            0.9,
            (147,58,31),
            1
        )

        cv2.imshow("Demo", frame)

        if is_pressed(" "):
            number_of_datapoints = 21

        if number_of_datapoints > 0:
            list_of_points.append(take_point(left_pupil, right_pupil, middle_pupil))
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
