import json
import logging
import os

def load_attack_details():
    """
    Loads attack details from a JSON file.
    """
    logging.info("Loading attack details...")
    utils_dir = os.path.dirname(__file__)
    json_path = os.path.join(utils_dir, 'attack_details.json')
    try:
        with open(json_path, 'r') as f:
            attack_details = json.load(f)
        logging.info("Successfully loaded attack details from JSON file")
        return attack_details
    except FileNotFoundError:
        logging.error(f"Error: attack_details.json not found in {json_path}")
        return {}
    except json.JSONDecodeError as e:
        logging.error(f"Error parsing attack_details.json: {e}")
        return {}

attack_details = load_attack_details()