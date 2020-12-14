import flask
from flask import request, jsonify
from markupsafe import escape
import spacy
import yaml


app = flask.Flask(__name__)

with open("config.yaml", 'r') as stream:
    try:
        config = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

print('Launching flask server with config:', config)

app.config.from_mapping(config)

model = spacy.load(config['MODEL_PATH'])

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Intent</h1>'''


@app.route('/api/intent', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    response = None
    if 'sentence' in request.args:
        sentence = str(escape(request.args['sentence']))
        doc = model(sentence)
        response = {k: round(v, 4) for k,v in doc.cats.items()}
    else:
        return "Error: No sentence field provided. Please specify a sentence."

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(response)

app.run(host=config['HOST'], port=config['PORT'])