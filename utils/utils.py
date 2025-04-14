import json


#TODO: handle Exceptions that rise from those
import ast
import json
import ast
import json
import queue
import atexit
import re
import logging

def extract_json_from_llm_response(response_content):
    # Try to locate the JSON part
    json_start = response_content.find("```json")
    json_end = response_content.rfind("```")
    
    if json_start != -1 and json_end != -1 and json_end > json_start:
        # If there's a JSON block, extract it
        json_string = response_content[json_start + len("```json"):json_end].strip()
    else:
        # No explicit block, try to extract the first valid JSON-like content
        match = re.search(r'{.*}', response_content, re.DOTALL)
        if match:
            json_string = match.group(0).strip()
        else:
            json_string = response_content.strip()
    
    try:
        # Try to load the cleaned string as JSON
        parsed_json = json.loads(json_string)
        return parsed_json
    except json.JSONDecodeError:
        try:
            # Fallback to handling Python-style dictionaries
            parsed_json = ast.literal_eval(json_string)
            return parsed_json
        except (SyntaxError, ValueError) as e:
            raise ValueError(f"Error parsing JSON: {e}\nExtracted string: {json_string}")

def get_prompt(name, **kwargs):
    with open("prompts.json", "r") as file:
        PROMPTS = json.load(file)

    prompt_data = PROMPTS.get(name)
    if not prompt_data:
        raise ValueError(f"Prompt '{name}' not found!")
    
    prompt_text = prompt_data["prompt"].format(**kwargs)
    
    return prompt_text

def get_json_response_format(name, **kwargs):
    with open("prompts.json", "r") as file:
        PROMPTS = json.load(file)

    prompt_data = PROMPTS.get(name)
    if not prompt_data:
        raise ValueError(f"format '{name}' not found!")
    
    json_format = prompt_data.get("json_response_format")
    if not json_format:
        raise ValueError(f"JSON response format not found for prompt '{name}'")

    return json_format

def _get_logging_setup():
    with open("config.json", "r") as file:
        CONFIG = json.load(file)
    logging_setup = CONFIG.get("logger_setup")

    if not logging_setup:
        raise ValueError(f"format 'logger_setup' not found!")
    
    log_queue = queue.Queue(-1)
    logging_setup["handlers"]["queue_handler"]["queue"] = log_queue
    
    
    return logging_setup

def setup_logging():
    logging.config.dictConfig(_get_logging_setup())
    # queue_handler = logging.getHandlerByName("queue_handler")
    # if queue_handler is not None:
    #     queue_handler.listener.start()
    #     atexit.register(queue_handler.listener.stop)

    