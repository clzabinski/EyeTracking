import csv
import os.path
import time

header = ["Left Pupil", "Right Pupil", "Nose Bridge"]


def take_point(left_pupil, right_pupil, middle_pupil):
    print(f"Taking datapoints: {left_pupil}, {right_pupil}, {middle_pupil}")
    DPDict = {
        'Left': left_pupil,
        'Right': right_pupil,
        'Nose': middle_pupil
    }

    return middle_pupil

    file_exists = os.path.isfile('gaze_data.csv')
    with open('gaze_data.csv', 'a', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=header)
        if not file_exists:
            writer.writeheader()
        writer.writerow(row)

    time.sleep(0.1)
