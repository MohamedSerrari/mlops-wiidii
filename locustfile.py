import urllib
import json
import random
from locust import HttpUser, task

with open("./data/testing_set.json", encoding='utf8', errors='ignore') as file:
    sentences = json.load(file)

class IntentionTestUser(HttpUser):
    @task
    def intent_api(self):
        for _ in range(0, 10):
            sentence = random.choice(sentences)
            url = "/api/intent?{}".format(urllib.parse.urlencode(sentence))
            self.client.get(url)
