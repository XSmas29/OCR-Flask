
from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
import os
import torch
import cv2
import keras_ocr

app = Flask(__name__)
app.debug = True
uploads_dir = os.path.join(app.instance_path, 'uploads')

ocr_th = 0.3
recognizer = keras_ocr.recognition.Recognizer(
    #weights='kurapan'
)