"""
This script converts a dataset from PASCAL VOC format to YOLO format. The dataset is located in a directory called "DATASET" and contains a train.csv file, which has information about the image file name and the bounding box coordinates for the objects in the image.

The script does the following steps:

- Loads the train.csv file into a pandas dataframe
- Fixes bounding box coordinates that are outside of the image resolution
- Creates a new directory called "yolo_data" and copies the image files to this new directory
- Goes through each image and creates a new .txt file for each image, in which it writes the class ID and the bounding box coordinates in YOLO format.
- Prints a message to indicate that the data conversion is completed
"""


import os
import pandas as pd
import cv2
import shutil

# Define the path to the dataset
data_path = "DATASET"

# Load the train.csv file
train_df = pd.read_csv(os.path.join(data_path, "train.csv"))

# Fix BBOX Coords as per resolution 960x540 (some data are ploting BBOX outside the image)
def fix_bounding_box(df):
    counter = 0
    for i in range(df.shape[0]):
        if df.loc[i, 'xmax'] > 960:
            df.loc[i, 'xmax'] = 960
            counter += 1
        if df.loc[i, 'xmin'] < 0:
            df.loc[i, 'xmin'] = 0
            counter += 1
        if df.loc[i, 'ymax'] > 540:
            df.loc[i, 'ymax'] = 540
            counter += 1
        if df.loc[i, 'ymin'] < 0:
            df.loc[i, 'ymin'] = 0
            counter += 1
    print(f'{counter} bounding boxes were fixed.')
    return df

train_df = fix_bounding_box(train_df)

# Create a new directory to store the YOLO format data
yolo_data_path = os.path.join('./', "yolo_data")
if not os.path.exists(yolo_data_path):
    os.mkdir(yolo_data_path)
    
# Create a new directory to store the images
train_path = os.path.join(yolo_data_path, "train")
if not os.path.exists(train_path):
    os.mkdir(train_path)
    
# Copy the images to the new directory
for image_name in train_df["image_path"].unique():
    image_path = os.path.join(data_path, "images", image_name)
    new_image_path = os.path.join(train_path, image_name)
    # os.system(f"copy {image_path} {new_image_path}")
    shutil.move(image_path,new_image_path)

# pascal voc to yolo
def voc2yolo(coords, img_w, img_h):
    xmin, ymin, xmax, ymax = coords
    center_x = (xmin + (xmax-xmin)/2)/img_w
    center_y = (ymin + (ymax-ymin)/2)/img_h
    width = (xmax-xmin)/img_w
    height = (ymax-ymin)/img_h
    return [center_x, center_y, width, height]


# Create a new .txt file for each image
for image_name in train_df["image_path"].unique():
    image_data = train_df[train_df["image_path"] == image_name]
    img = cv2.imread(os.path.join(train_path, image_name))
    txt_path = os.path.join(train_path, f"{image_name.split('.')[0]}.txt")
    with open(txt_path, "w") as f:
        for index, row in image_data.iterrows():
            class_id = int(row["class"])
 # type: ignore
            xmin = row["xmin"]
            ymin = row["ymin"]
            xmax = row["xmax"]
            ymax = row["ymax"]
            center_x, center_y, width, height = voc2yolo([xmin, ymin, xmax, ymax],960,540)
            f.write(f"{class_id} {center_x} {center_y} {width} {height}\n")

print('Data conversion completed!')
