# Submision
"""
The script reads the predicted labels from folder and generates the submission file.
It takes the predicted class_id, center_x, center_y, width and height and convert them into xmin, ymin, xmax and ymax.
It then add the data to the sample submission file and generates the final submission file.
"""

import warnings
warnings.filterwarnings("ignore")
import os
import pandas as pd
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("-p", "--path", type=str, help="path of yolo formated dataset")
args = parser.parse_args()


classes = ['GRAFFITI','FADED_SIGNAGE','POTHOLES','GARBAGE','CONSTRUCTION_ROAD','BROKEN_SIGNAGE','BAD_STREETLIGHT','BAD_BILLBOARD','SAND_ON_ROAD','CLUTTER_SIDEWALK','UNKEPT_FACADE']

folder = args.path
submission = pd.read_csv('dataset/sample_submission.csv')

height_, width_ = 960,540

for file in os.listdir(folder):
    if file.endswith(".txt"):
        image_name = file.split(".")[0]+'.jpg'
        with open(os.path.join(folder, file)) as f:
            lines = f.readlines()
        for line in lines:
            line_data = line.split(" ")

            class_id = int(line_data[0])
            class_name = classes[class_id]
            center_x = float(line_data[1])
            center_y = float(line_data[2])
            width = float(line_data[3])
            height = float(line_data[4])

            xmin = int((float(center_x) - float(width)/2) * width_)
            ymin = int((float(center_y) - float(height)/2) * height_)
            xmax = int((float(center_x) + float(width)/2) * width_)
            ymax = int((float(center_y) + float(height)/2) * height_)

            # add the data to the list
            row = pd.Series([class_id, image_name, class_name, xmax, xmin, ymax, ymin], index = submission.columns)
            submission = submission.append(row, ignore_index=True)

submission.to_csv('submission.csv',index=False)