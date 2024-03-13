import requests
import utils
import configurations as config


def get_output_from_model(system_prompt, user_prompt, temperature=0.9):
    url = f'{config.GPT_URL}{config.GPT_USAGE_ENDPOINT}'

    headers = {
        'Authorization': f'Bearer {config.TOKEN}',
        'Content-Type': 'application/json'
    }

    data = {'messages': [
        {'role': 'system', 'content': system_prompt},
        {'role': 'user', 'content': user_prompt}
    ],
        'model_id': config.GPT35_TURBO_MODEL,
        'temperature': temperature}

    response = requests.post(url, headers=headers, json=data)

    output = None
    if response.ok:
        response = response.json()
        first_choice = response.get('choices')[0]
        output = first_choice.get('message', {}).get('content')

    return output
