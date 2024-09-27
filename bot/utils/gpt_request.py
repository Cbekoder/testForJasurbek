from loader import client
import json

def send_request(prompt):
    response = client.chat.completions.create(
        messages=[{
            "role": "user",
            "content": prompt,
        }],
        model="gpt-4o-mini",
    )
    result = json.loads(response.json())
    return result['choices'][0]['message']['content']