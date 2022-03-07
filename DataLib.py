import csv
import os.path

header = ["Left Pupil", "Right Pupil", "Horizontal Value", "Vertical Value", "Gaze Location"]


def take_point(left_pupil, right_pupil, horiz_val, vert_val, gaze_location):
    row = {
        'Left Pupil': left_pupil,
        'Right Pupil': right_pupil,
        'Horizontal Value': horiz_val,
        'Vertical Value': vert_val,
        'Gaze Location': gaze_location
    }

    file_exists = os.path.isfile('gaze_data.csv')
    with open('gaze_data.csv', 'a', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=header)
        if not file_exists:
            writer.writeheader()
        writer.writerow(row)