import flask
from flask import request, jsonify
from markupsafe import escape
import spacy
from utils import load_config, round_output
import logging

config = load_config('config.yaml')

app = flask.Flask(__name__)
app.logger.setLevel(logging.ERROR)

nlu = spacy.load(config['MODEL_PATH'])
other_pipes = [pipe for pipe in nlu.pipe_names if pipe != "textcat"]

@app.route('/api/intent', methods=['GET'])
def intent_api():

    if 'sentence' in request.args:
        with nlu.disable_pipes(*other_pipes):
            sentence = str(escape(request.args['sentence']))
            output = nlu(sentence)
    else:
        return "Error: No sentence field provided. Please specify a sentence."

    return jsonify(round_output(output))

app.run(host=config['HOST'], port=config['PORT'], debug=config['DEBUG'])