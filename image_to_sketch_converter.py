# -*- coding: utf-8 -*-
"""Image_to_sketch_converter.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EahSYt2Si-ErUQbLS9ysdmEYone3NlUR
"""

import cv2

import numpy as np
import pandas as pd
import cv2 as cv
from google.colab.patches import cv2_imshow
from skimage import io
from PIL import Image
import matplotlib.pylab as plt

!pip install cv

from google.colab import files
uploaded = files.upload()

import cv2
image = cv2.imread("cute.jpg")
cv2_imshow(image)
cv2.waitKey(0)

files.download('cute.jpg')

import os
os.listdir()

!pip install -U -q PyDrive

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from google.colab import auth
from oauth2client.client import GoogleCredentials

auth.authenticate_user()
gauth = GoogleAuth()
gauth.credentials = GoogleCredentials.get_application_default()
drive = GoogleDrive(gauth)

import cv2
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2_imshow(gray_image)
cv2.waitKey(0)

inverted_image = 245 - gray_image
cv2_imshow(inverted_image)
cv2.waitKey()

blurred = cv2.GaussianBlur(inverted_image, (25, 25), 0)

inverted_blurred = 250 - blurred
pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)
cv2_imshow(pencil_sketch)
cv2.waitKey(0)