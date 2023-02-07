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


if __name__ == "__main__":
    payload = config.PAYLOAD_TTS
    payload["text"] = "Xin chào Sài Gòn. Hôm nay đặc biệt là 1 ngày đầy nắng gió bão bùng.Xin chào Sài Gòn. Hôm nay đặc biệt là 1 ngày đầy nắng gió bão bùng."
    payload["voice_id"] = 1
    t = time.time()
    audio_file = text_to_speech(payload)
    print(time.time() - t)
    print(audio_file)