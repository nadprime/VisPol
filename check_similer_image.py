# Check for repeated/similar images

import os
import imagehash
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("-p", "--path", type=str, help="path of yolo formated dataset")
args = parser.parse_args()

folder = args.path

hashes = {}
filenames = []

for filename in os.listdir(folder):
    if filename.endswith('.jpg'):
        image = Image.open(os.path.join(folder, filename))
        hash_value = str(imagehash.phash(image))
        hashes[filename] = hash_value

for key, value in hashes.items():
    for key2, value2 in hashes.items():
        if key != key2:
            if value == value2:
                filenames.append(key)
                filenames.append(key2)

filenames = set(filenames)

print(len(filenames))  
if len(filenames):
    # subplot with a grid of 4x4
    fig, axes = plt.subplots(4, 4, figsize=(8, 6))
    axes_list = [item for sublist in axes for item in sublist]

    for i, filename in enumerate(list(filenames)[:16]):
        img = mpimg.imread(os.path.join(folder, filename))
        axes_list[i].imshow(img)
        axes_list[i].axis('off')
    plt.show()
