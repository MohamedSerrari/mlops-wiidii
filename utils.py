import yaml
# from flask import jsonify
import json


def load_config(config_path='config.yaml'):
    with open(config_path, 'r') as stream:
        try:
            config = yaml.safe_load(stream)
            print('Launching server with config:', config)
        except yaml.YAMLError as exc:
            print(exc)

    return config

def round_output(model_output):
    return {k: round(v, 4) for k,v in model_output.cats.items()}

