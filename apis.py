import requests
import config
import os
import time


def text_to_speech(payload):
    url = config.TTS_URL
    response = requests.post(url, json=payload, headers=config.HEADRER)
    try:
        audio_file = os.path.basename(response.json()["audio_path"])
    except:
        audio_file = None
    return audio_file

def speech_to_text(file_path):
    url = config.STT_URL
    file = {"file": open(file_path, "rb")}
    response = requests.post(url, files=file)
    try:
        text = response.json()["data"]["item"]["text"]
    except:
        text = None
    return text

def clip(payload):
    url = config.CLIP_URL
    response = requests.post(url, json=payload, headers=config.HEADRER)
    try:
        image_list = response.json()["image"]
    except:
        image_list = None
    return image_list


if __name__ == "__main__":
    t = time.time()
    audio_file = speech_to_text("resources/Audio/test.mp3")
    print(time.time() - t)
    print(audio_file)