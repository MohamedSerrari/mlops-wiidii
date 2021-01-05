# Creating NLU API for intent classification

## This repo contains multiple notebooks and files dealing with the problematics we faced while creating an NLU API for intent classification.

Q1. Analysing the training and evaluation data.

Q2. Evaluating a pretrained model.

Q3. Training and testing our own pipeline using spaCy.

LOSS       P        R        F1
0.096    0.860    0.857    0.858

### Q4. Using FastAPI web framework to provide APIs to our intention model.

Build docker image
```shell
docker build --tag intentclassication .
```

Run docker image
```shell
docker run -d -p 8000:8000 intentclassication
```

Server is now listening on http://localhost:8000.

- To check documentation of the API, check [http://localhost:8000/docs](http://localhost:8000/docs)
- To test the API, check [http://localhost:8000/api/intent/?sentence=J%27ai%20besoin%20d%27un%20restaurant%20italien%20pour%20ce%20soir,%20nous%20serons%204%20convives](http://localhost:8000/api/intent/?sentence=J%27ai%20besoin%20d%27un%20restaurant%20italien%20pour%20ce%20soir,%20nous%20serons%204%20convives)

The image is also available on DockerHub: [link](https://hub.docker.com/repository/docker/csj0oe/mlops-wiidii)

### Performance testing
We are using [Uvicorn](https://www.uvicorn.org/), an ASGI server implementation, using uvloop and httptools.
We used Locust as a testing tool. 
We configured Locust to simulate 1000 users with spawn rate equals to 10 users per second.
The screenshot below depicts the test result.
![Locust stats](scrots/locust_stats.png)
![Locust](scrots/locust.png)
