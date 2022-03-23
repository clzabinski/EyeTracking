"""
Demonstration of the GazeTracking library.
Check the README.md for complete documentation.
"""

import cv2
from keyboard import is_pressed
from gaze_tracking import GazeTracking
from DataLib import take_point


def main():
    gaze = GazeTracking()
    webcam = cv2.VideoCapture(0)

    take_info = True

    number_of_datapoints = 0

    while True:
        # We get a new frame from the webcam
        _, frame = webcam.read()

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
        horizontal_value = gaze.horizontal_ratio()
        vertical_value = gaze.vertical_ratio()
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
            "Horizontal Value: " + str(horizontal_value),
            (90, 200),
            cv2.FONT_HERSHEY_DUPLEX,
            0.9,
            (147, 58, 31),
            1,
        )
        cv2.putText(
            frame,
            "Vertical Value: " + str(vertical_value),
            (90, 235),
            cv2.FONT_HERSHEY_DUPLEX,
            0.9,
            (147, 58, 31),
            1,
        )

        cv2.imshow("Demo", frame)

        if is_pressed(" "):
            number_of_datapoints = 21

        if number_of_datapoints > 0:
            take_point(left_pupil, right_pupil, horizontal_value, vertical_value, text)
            number_of_datapoints -= 1

        if cv2.waitKey(1) == 27:
            break

    webcam.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
