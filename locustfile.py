import urllib
import json
import random
from locust import HttpUser, task

class IntentionTestUser(HttpUser):
    @task
    def intent_api(self):
        with open("./data/testing_set.json") as file:
            sentences = json.load(file)
        for _ in range(0, 10):
            sentence = random.choice(sentences)
            url = "/api/intent/?{}".format(urllib.parse.urlencode(sentence))
            self.client.get(url)
