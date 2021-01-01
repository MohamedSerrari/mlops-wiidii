from fastapi import FastAPI
import spacy
import uvicorn

app = FastAPI(title="Idiwii intention classification model",
              description="Using NLU in order to understand and classify a user's intention",
              version="1.0")

nlu = spacy.load("./model_save")

@app.get("/api/intent/")
async def intent_api(sentence: str):
    other_pipes = [pipe for pipe in nlu.pipe_names if pipe != "textcat"]
    with nlu.disable_pipes(*other_pipes):
        predict = nlu(sentence)

    return predict.cats

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000, reload=False, access_log=False)
