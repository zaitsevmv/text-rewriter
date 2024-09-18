import os
import requests
import json
import uuid

import requests
import os

def first_request(text):
    url = "https://ai-based-article-rewriter.p.rapidapi.com/data"

    payload = f"-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"text\"\r\n\r\n{text}\r\n-----011000010111000001101001--\r\n\r\n"
    payload = payload.encode('utf-8')  

    headers = {
        "x-rapidapi-key": os.getenv("RAPID_KEY"),
        "x-rapidapi-host": "ai-based-article-rewriter.p.rapidapi.com",
        "Content-Type": "multipart/form-data; boundary=---011000010111000001101001"
    }

    # Make the request with the payload encoded in UTF-8
    response = requests.request("POST", url, data=payload, headers=headers)
    
    if response.status_code == 200:
        return response.text
    else:
        return ""

    
def second_request(text):
    def get_access_token():
        request_id = uuid.uuid4()
        url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"
        payload = 'scope=GIGACHAT_API_PERS'
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'application/json',
            'RqUID': request_id.__str__(),
            'Authorization': f'Basic {os.environ.get("GIGACHAT_KEY")}'
        }
        response = requests.request("POST", url, headers=headers, data=payload, verify=False)
        return response.json()['access_token']

    access_token = get_access_token()

    url = "https://gigachat.devices.sberbank.ru/api/v1/chat/completions"
    payload = json.dumps({
        "model": "GigaChat",
        "messages": [
            {
                "role": "user",
                "content": f"Paraphrase this text. Text: {text}"
            }
        ],
        "stream": False,
        "repetition_penalty": 1
    })
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': f'Bearer {access_token}'
    }
    response = requests.request("POST", url, headers=headers, data=payload, verify=False)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return ""