import json


#TODO: handle Exceptions that rise from those
def extract_json_from_llm_response(response_content):
    json_start = response_content.find("```json")
    json_end = response_content.rfind("```")
    
    if json_start != -1 and json_end != -1 and json_end > json_start:
        json_string = response_content[json_start + len("```json"):json_end].strip()
    else:
        json_string = response_content.strip()
    
    try:
        parsed_json = json.loads(json_string)
        return parsed_json
    except json.JSONDecodeError as e:
        raise ValueError(f"Error parsing JSON: {e}\nExtracted string: {json_string}")
    
def get_prompt(name, **kwargs):
    with open("prompts.json", "r") as file:
        PROMPTS = json.load(file)

    prompt_data = PROMPTS.get(name)
    if not prompt_data:
        raise ValueError(f"Prompt '{name}' not found!")
    
    prompt_text = prompt_data["prompt2"].format(**kwargs)

    return prompt_text