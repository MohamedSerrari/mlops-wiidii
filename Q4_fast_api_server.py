from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
import spacy
import uvicorn
from utils import load_config, round_output

config = load_config('config.yaml')

app = FastAPI(title="Idiwii intention classification model",
              description="Using NLU in order to understand and classify a user's intention",
              version="1.0")

nlu = spacy.load("./model_save")

@app.get("/api/intent")
async def intent_api(sentence: str):
    other_pipes = [pipe for pipe in nlu.pipe_names if pipe != "textcat"]
    with nlu.disable_pipes(*other_pipes):
        output = nlu(sentence)

    return jsonable_encoder(round_output(output))

if __name__ == "__main__":
    uvicorn.run(app, host=config['HOST'], port=config['PORT'], debug=config['DEBUG'], reload=False, access_log=False)
