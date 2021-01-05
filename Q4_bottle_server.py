import bottle
import spacy
import json
from utils import load_config, round_output

config = load_config('config.yaml')

nlu = spacy.load(config['MODEL_PATH'])

@bottle.route("/api/intent")
def intent_api() :
    sentence = bottle.request.query['sentence']
    other_pipes = [pipe for pipe in nlu.pipe_names if pipe != "textcat"]
    with nlu.disable_pipes(*other_pipes):
        output = nlu(sentence)
    bottle.response.content_type = "application/json"
    return round_output(output)

bottle.run(bottle.app(), host=config['HOST'], port=config['PORT'], debug=config['DEBUG'], reloader=True)
