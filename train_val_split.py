"""
This script divides the dataset into two parts, train and validation. It moves the image and annotation files to their respective folders and generates a YAML data configuration file.
"""

import os
import random
import yaml

# Path to the dataset
dataset_root = r"yolo_data"
dataset_path = r"yolo_data/train"

# List all image and annotation files in the dataset
data_files = [f for f in os.listdir("yolo_data/train") if f.endswith(".jpg")]

# remove .jpg from the file names
data_files = [f[:-4] for f in data_files]

# Randomly shuffle the list
random.shuffle(data_files)

# Split the list into two parts
split_p = 0.90

split_idx = int(len(data_files) * split_p)
train, val = data_files[:split_idx], data_files[split_idx:]

# Create train and val folders
train_path = os.path.join(dataset_root, "train")
val_path = os.path.join(dataset_root, "valid")
os.makedirs(train_path, exist_ok=True)
os.makedirs(val_path, exist_ok=True)

# Move train and val files
for f in train:
    os.rename(f"{dataset_path}/{f}.jpg", f"{train_path}/{f}.jpg")
    os.rename(f"{dataset_path}/{f}.txt", f"{train_path}/{f}.txt")

for f in val:
    os.rename(f"{dataset_path}/{f}.jpg", f"{val_path}/{f}.jpg")
    os.rename(f"{dataset_path}/{f}.txt", f"{val_path}/{f}.txt")

# Class labels
classes = ['GRAFFITI','FADED_SIGNAGE','POTHOLES','GARBAGE','CONSTRUCTION_ROAD','BROKEN_SIGNAGE','BAD_STREETLIGHT','BAD_BILLBOARD','SAND_ON_ROAD','CLUTTER_SIDEWALK','UNKEPT_FACADE']

# Save YAML Data Config File
with open(dataset_root+"/classes.txt", "w") as file:
    for c in classes:
        file.write(c + "\n")

with open(os.path.join(dataset_root, "data.yaml"), 'w') as f:
    yaml.dump(
        {
            'path': dataset_root,
            'train': "train",
            'val': "valid",
            'nc':  len(classes),
            'names': classes,
        },

        f,
        default_flow_style=False
    )
