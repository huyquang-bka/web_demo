import base64
import cv2
import numpy as np

def base64_to_image(base64_string):
    imgdata = base64.b64decode(base64_string)
    image = cv2.imdecode(np.frombuffer(imgdata, np.uint8), cv2.IMREAD_COLOR)
    return image