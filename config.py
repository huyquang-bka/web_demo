#TTS
TTS_HOST = '192.168.1.197'
TTS_PORT = 5001
TTS_URI = '/TTS'
TTS_URL = 'http://' + TTS_HOST + ':' + str(TTS_PORT) + TTS_URI
CONTENT_TYPE = "application/json"
HEADRER = {"Content-Type": CONTENT_TYPE}
PAYLOAD_TTS = {
  "text": "string",
  "voice_id": 0
}