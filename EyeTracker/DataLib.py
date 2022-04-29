import csv
import os.path
import time

header = ["Left", "Right", "Nose"]


def take_point(left_pupil, right_pupil, middle_pupil):
    print(f"Taking datapoints: {left_pupil}, {right_pupil}, {middle_pupil}")
    DPDict = {
        'Left': left_pupil,
        'Right': right_pupil,
        'Nose': middle_pupil
    }

    # return middle_pupil
    
    print(DPDict)

    file_exists = os.path.isfile('gaze_data.csv')
    with open('gaze_data.csv', 'a', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=header)
        if not file_exists:
            writer.writeheader()
        writer.writerow(DPDict)

    time.sleep(0.1)

    return middle_pupil
