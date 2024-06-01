import os
import requests

payload = {
    "animation_prompts": [
        {
            "frame": 0,
            "prompt": "a wide angle street level photo of a busy street in Versova, Mumbai, 4k, 8k, UHD",
        },
        {
            "frame": 10,
            "prompt": "a wide angle photo of the interiors of a bombay pub in the evening, neon lighting signs, cafe lighting, 4k, 8k, uhd",
        },
    ]
}

response = requests.post(
    "https://api.gooey.ai/v2/DeforumSD/",
    headers={
        "Authorization": "Bearer sk-aBaKrH70YFE7DWVDT4cVpFWHtR9bxNeqyCWhdQvfnqs9TYpK",
    },
    json=payload,
)
assert response.ok, response.content

result = response.json()
print(response.status_code, result)
