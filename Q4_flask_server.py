import flask
from flask import request, jsonify
from markupsafe import escape
import spacy
from utils import load_config, round_output

config = load_config('config.yaml')

app = flask.Flask(__name__)
app.config.from_mapping(config)

model = spacy.load(config['MODEL_PATH'])

@app.route('/api/intent', methods=['GET'])
def intent_api():

    if 'sentence' in request.args:
        sentence = str(escape(request.args['sentence']))
        output = model(sentence)
    else:
        return "Error: No sentence field provided. Please specify a sentence."

    return jsonify(round_output(output))

app.run(host=config['HOST'], port=config['PORT'], debug=config['DEBUG'])