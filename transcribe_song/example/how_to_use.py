import requests
import base64
import json
with open("tem.mp3", "rb") as f:
    bb = base64.b64encode(f.read()).decode('ascii')
url = 'http://127.0.0.1:8000/transcribe_song/'

myobj = {'base64_data': bb, 'song_id':69}

x = requests.post(url, data = myobj)

cc = x.json()["transcription"]
binf = base64.b64decode(cc.encode('ascii'))
open("out.mid", 'wb').write(binf)
