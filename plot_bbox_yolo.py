import argparse
import cv2
import os


parser = argparse.ArgumentParser()
parser.add_argument("-p", "--path", type=str, help="path of yolo formated dataset")

args = parser.parse_args()
# Set the path to the dataset folder
dataset_path = args.path

def plot_one_box(coords, img, color=(0, 255, 0), label=None, line_thickness=2):
    xmin, ymin, xmax, ymax = coords
    cv2.rectangle(img, (xmin, ymin), (xmax, ymax), color, line_thickness)
    if label is not None:
        text_size = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, .5, 2)[0]
        cv2.rectangle(img, (xmin, ymin - int(1.5*text_size[1])), (xmin + text_size[0], ymin), color, -1)
        cv2.putText(img, label, (xmin, ymin - int(.5*text_size[1])), cv2.FONT_HERSHEY_SIMPLEX, .5, (0,0,0), 2)
    return img

# Get a list of all the images in the dataset folder
image_list = [f for f in os.listdir(dataset_path) if f.endswith(".jpg")][:10]

# Iterate through the list of images
for image_name in image_list:
    # Load the image
    image = cv2.imread(os.path.join(dataset_path, image_name))

    # Read bounding box from annotation file
    with open(os.path.join(dataset_path, image_name.split(".jpg")[0]+".txt")) as f:
        lines = f.readlines()
        for line in lines:
            class_id, x_center, y_center, width, height = line.strip().split()
            height_, width_, _ = image.shape
            xmin = int((float(x_center) - float(width)/2) * width_)
            ymin = int((float(y_center) - float(height)/2) * height_)
            xmax = int((float(x_center) + float(width)/2) * width_)
            ymax = int((float(y_center) + float(height)/2) * height_)
            image = plot_one_box([xmin, ymin, xmax, ymax], image, label=class_id)

    # Display the image
    cv2.imshow("Image", image)
    cv2.waitKey(0)
