import requests
import novel_details
import utils
import configurations as config


system_prompt = utils.get_system_prompt(novel_details.novel_inputs)
print(system_prompt)


url = f'{config.GPT_URL}{config.GPT_USAGE_ENDPOINT}'

prompt = 'Give me the chapter details. Total chapter is 20'

headers = {
    'Authorization': f'Bearer {config.TOKEN}',
    'Content-Type': 'application/json'
}

data = {'messages': [
    {'role': 'system', 'content': system_prompt},
    {'role': 'user', 'content': prompt}
],
    'model_id': config.GPT35_TURBO_MODEL,
    'temperature': 0.7}


response = requests.post(url, headers=headers, json=data)

output = None

if response.ok:
    response = response.json()
    first_choice = response.get('choices')[0]
    output = first_choice.get('message', {}).get('content')

if output:
    print(output)
