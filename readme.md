# Visual Pollution Detection

This project is about detecting visual pollution from images using deep learning. We have used object detection algorithms to detect different types of visual pollution and classify them. The algorithm is trained using various datasets and converted into onnx format for faster computation.

# Detection and evaluation of the following elements on street imagery taken from a moving vehicle

Since visual pollution is a relatively recent issue compared to other forms of environmental contamination, study is needed to define, formalize, measure, and evaluate it from many angles. This competition aims to establish a new field of automated visual pollution classification, utilizing the technological prowess of the twenty-first century for environmental management applications.
By training and testing approaches to convolutional neural networks, we expect competitors to simulate the human learning experience in the context of picture identification for the classification of visual pollutants.
Additionally this will be useful for the development of a "visual pollution score/index" for urban areas that might produce a new "metric" or "indicator" in the discipline of urban environmental management.
In this competition, you will build and optimize algorithms based on a large-scale dataset. This dataset features the raw sensor camera inputs as perceived by a fleet of multiple vehicles in arestricted geographic area in KSA
If successful, you’ll make a significant contribution towards stimulating further development city planning and empowering communities around the world.


<p align="center">
<img width="895" alt="Screenshot_20230122_174442" src="https://user-images.githubusercontent.com/103782863/222286968-6f98fdab-42ac-4652-bf81-ecede2c00f81.png">
</p>

<p align="center">
<img width="940" alt="output" src="https://user-images.githubusercontent.com/103782863/222291060-3dc77ddd-862b-47ca-bbbb-21916feca180.png">
</p>

YouTube Video [Click Here](https://youtu.be/YOiUuPmjllw)
</br>

</br>

## Installation

The project is written in Python and the following libraries are required to run the project:

- Torch
- Numpy
- Opencv
- Streamlit

## Usage

To run the project, first clone the repository and then install the requirements:

```bash
python  -m venv env
env/Scripts/activate
pip install -r .\requirements.txt
```

To run the web app use the following command:

```bash
cd app
streamlit run app.py
```
