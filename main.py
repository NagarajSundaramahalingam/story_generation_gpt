import requests
import configurations as config


SYSTEM_PROMPT = 'Your job is to generate story/novel based on the inputs provided.  '

url = f'{config.GPT_URL}{config.GPT_USAGE_ENDPOINT}'
prompt = 'A graduated guy is going to a first day in job. Give me more details for chapter 1. With Dialogue of 40%'

headers = {
    'Authorization': f'Bearer {config.TOKEN}',
    'Content-Type': 'application/json'
}
data = {'messages': [
    {'role': 'system', 'content': SYSTEM_PROMPT},
    {'role': 'user', 'content': prompt}
],
    'model_id': config.GPT4_MODEL}


response = requests.post(url, headers=headers, json=data)


print(response.json())
