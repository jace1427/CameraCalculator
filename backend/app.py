import os
import hashlib
from waitress import serve
from flask import Flask, render_template, jsonify, request, url_for
from flask_cors import CORS

from cv import image_compute

app = Flask(__name__)
CORS(app)

@app.route('/uploader', methods = ['GET', 'POST'])
def uploader():
    if request.method == 'POST':
        f = request.files['file']
        filename, file_extension = os.path.splitext(f.filename)
        hashed_filename = hashlib.sha256(filename.encode()).hexdigest()[:15]
        f.save(os.environ['UPLOAD_FOLDER'] + hashed_filename)
        print('[POST]\tRecieved: {}'.format(hashed_filename))
        return hashed_filename
    else:
        return 'None'

@app.route('/<filehash>', methods = ['GET'])
def results(filehash):
    if os.path.exists(os.environ['UPLOAD_FOLDER'] + filehash):
        image = open(os.environ['UPLOAD_FOLDER'] + filehash)
        result = image_compute(image)
        return result
    else:
        return 'None'

if __name__ == "__main__":
    print('Backend application is live')
    serve(app, host='0.0.0.0', port=3000)
