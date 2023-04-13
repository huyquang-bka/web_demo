from flask import Flask, render_template, request, jsonify
import cv2
import base64
import numpy as np


def base64_to_image(base64_string):
    imgdata = base64.b64decode(base64_string)
    image = cv2.imdecode(np.frombuffer(imgdata, np.uint8), -1)
    return image

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/post-image', methods=['POST'])
def post_image():
    data = request.get_json()
    image = data['image']
    new_image = base64_to_image(image)
    cv2.imwrite('image.jpg', new_image)
    return jsonify({'status': 'success'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=50002, debug=False)

