# Creating NLU API for intent classification

## This repo contains multiple notebooks and files dealing with the problematics we faced while creating an NLU API for intent classification.

Q1. Analysing the training and evaluation data.

Q2. Evaluating a pretrained model.

Q3. Training and testing our own pipeline using spaCy.

Q4. Using FastAPI web framework to provide APIs to our intention model.

### Performance testing
We are using [Uvicorn](https://www.uvicorn.org/), an ASGI server implementation, using uvloop and httptools.
We used Locust as a testing tool. 
We configured Locust to simulate 1000 users with spawn rate equals to 10 users per second.
The screenshot below depicts the test result.
![Locust stats](scrots/locust_stats.png)
![Locust](scrots/locust.png)
