from http.client import responses

import requests
def chat_message_request():
    url = "http://192.168.60.37:7088/arcana-llm-service/v1/chat-messages"

    headers = {
        "Authorization": "Bearer app-hAOPgCwy0mVxDLsvGvVaXwQw",
        "Content-Type": "application/json",
    }
    data = {
        "inputs": {},
        "user": "abc-123",
        "query": "What are the specs of the iPhone 13 Pro Max?",
        "response_mode": "streaming"
    }

    response = requests.post(url, headers=headers, json=data)

    # For streaming response, you might want to handle it differently
    if data["response_mode"] == "streaming":
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                print(chunk.decode('utf-8'), end='')
    else:
        print(response.status_code)
        print(response.json())