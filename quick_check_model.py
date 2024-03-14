import model_operations


system_prompt = 'Your job is to generate a story with more descriptive as paragraph'

user_prompt = 'A Business man got a time machine. What is the impact of that to this world. Generate a story for this.'

result = model_operations.get_output_from_model(system_prompt, user_prompt)


print(result)
