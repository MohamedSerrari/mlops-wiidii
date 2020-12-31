from fastapi import FastAPI
import spacy

app = FastAPI()
nlu = spacy.load("./model_save")

@app.get("/api/intent/")
async def intent_api(sentence: str):
    other_pipes = [pipe for pipe in nlu.pipe_names if pipe != "textcat"]
    with nlu.disable_pipes(*other_pipes):
        predict = nlu(sentence)

    return predict.cats
