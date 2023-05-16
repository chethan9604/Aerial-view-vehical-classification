import time
from absl import app, logging
import cv2
import numpy as np
from flask import Flask, request, Response, jsonify, send_from_directory, abort, render_template,send_file
import os
import sys
from subprocess import call
from detect import *
from flask_cors import CORS
import shutil


app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
   return render_template('index.html')


@app.route('/test', methods= ['POST'])
def get_image():
   inp_path = '/static/input/input.png'
   res_path = '/static/predicted/result.png'
   if os.path.exists(inp_path):       
      shutil.rmtree(inp_path)
      print('Removing previous Input files')
   if os.path.exists(res_path):
      shutil.rmtree(res_path)
      print('Removing previous Result files')
   image = request.files['inputfile']
   image.save('C:/Users/cpyreddy/Downloads/object-detection-app/object-detection-app/static/input/input.png')
   print('Saving Input Image')
   img = detect('C:/Users/cpyreddy/Downloads/object-detection-app/object-detection-app/static/input/input.png')
   cv2.imwrite('C:/Users/cpyreddy/Downloads/object-detection-app/object-detection-app/static/predicted/result.png' , img)
   print('Creating Detection files')
   filename1 =  'static/input/input.png'
   filename2 = 'static/predicted/result.png'
   print('done')
   return render_template('index.html',filename1=filename1, filename2 = filename2)

if __name__ == '__main__':
    app.run(debug=True)
