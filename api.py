import os
import requests
import json
import uuid
import time 

import requests
import os

def first_request(text):
    url = "https://ai-based-article-rewriter.p.rapidapi.com/data"

    payload = f"-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"text\"\r\n\r\n{text}\r\n-----011000010111000001101001--\r\n\r\n"
    payload = payload.encode('utf-8')  

    headers = {
        "x-rapidapi-key": os.getenv("RAPID_KEY3"),
        "x-rapidapi-host": "ai-based-article-rewriter.p.rapidapi.com",
        "Content-Type": "multipart/form-data; boundary=---011000010111000001101001"
    }

    start = time.time()
    response = requests.request("POST", url, data=payload, headers=headers)

    print("Time elapsed:")
    print(time.time() - start)
    
    if response.status_code == 200:
        print(response.text)
        return response.text
    else:
        print(response.text)
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
        "model": "GigaChat-Pro",
        "messages": [
            {
                "role": "user",
                "content": f"Rewrite this text: {text}. Выводи только перефразированный текст."
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
    start = time.time()
    response = requests.request("POST", url, headers=headers, data=payload, verify=False)

    print("Time elapsed:")
    print(time.time() - start)

    if response.status_code == 200:
        print(response.text)
        return response.json()["choices"][0]["message"]["content"]
    else:
        print(response.text)
        return ""