import bottle
import spacy
import json

nlu = spacy.load("./model")

@bottle.route("/api/intent")
def intent_api() :
    sentence = bottle.request.query['sentence']
    other_pipes = [pipe for pipe in nlu.pipe_names if pipe != "textcat"]
    with nlu.disable_pipes(*other_pipes):
        predict = nlu(sentence)
    bottle.response.content_type = "application/json"
    return json.dumps(predict.cats)

bottle.run(bottle.app(), host='0.0.0.0', port=8080, debug= True, reloader=True)
