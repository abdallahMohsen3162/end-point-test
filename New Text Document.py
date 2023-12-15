import mimetypes
import os
from flask import Flask, send_file
from flask import request, jsonify
import cv2
import numpy as np
from ultralytics import YOLO
import matplotlib.pyplot as plt
import math
from flask import Flask, request
from flask_restful import Api, Resource
from flask import Flask, jsonify
from flask_cors import CORS
from flask import Flask, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
api = Api(app)
CORS(app)  # Enable CORS for all routes
imgname = "img.jpg"
original_image = cv2.imread(imgname)
app = Flask(__name__)


data = [
 
]

@app.route('/fet', methods=['GET', 'POST'])
@cross_origin(origin="http://localhost:3000")
def fet():
    images_directory = ''
    image_path = os.path.join(images_directory, imgname)
    mimetype, _ = mimetypes.guess_type(image_path)
    return send_file(image_path, mimetype=mimetype)
   
   
   
@app.route('/testapi', methods=['GET'])
@cross_origin(origin="http://localhost:3000")
def po():
 return jsonify({
  "name":"abdallah",
  "age":50
 })


if __name__ == '__main__':
    app.run(port=80)  # Use port 80