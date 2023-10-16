import requests
import json

url = 'http://0.0.0.0:50040'
req = {
    'session_id': '123',
    'scene_id': '1001',
    'text_q': 'abc',
    'text_a': 'edf'
}
req = json.dumps(req, ensure_ascii=False)

resp = requests.post(url, req)

