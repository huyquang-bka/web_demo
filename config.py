HOST = '192.168.1.197'
PORT = 5001
CONTENT_TYPE = "application/json"
HEADRER = {"Content-Type": CONTENT_TYPE}

#TTS
TTS_URI = '/api/v1/tts'
TTS_URL = 'http://' + HOST + ':' + str(PORT) + TTS_URI
PAYLOAD_TTS = {
  "text": "string",
  "voice_id": 0
}

#STT
STT_URI = '/api/v1/voice/1'
STT_URL = 'http://' + HOST + ':' + str(PORT) + STT_URI

#CLIP
CLIP_URI = '/api/v1/clip'
CLIP_URL = 'http://' + HOST + ':' + str(PORT) + CLIP_URI
PAYLOAD_CLIP = {
    "text": "",
    "num_image": 5
}



