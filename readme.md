# Visual Pollution Detection

This project is about detecting visual pollution from images using deep learning. We have used object detection algorithms to detect different types of visual pollution and classify them. The algorithm is trained using various datasets and converted into onnx format for faster computation.

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
