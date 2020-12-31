import urllib
from locust import HttpUser, task

class IntentionTestUser(HttpUser):
    sentences = [
        {"sentence": ""},
        {"sentence": "restaurant"},
        {"sentence": "j\'ai besoin d'un restaurant italien pour ce soir"},
        {"sentence": "j'ai besoin de la météo pour demain"},
        {"sentence": "j'ai besoin d'un hotel prés de moi"},
        {"sentence": "j'ai besoin d'un smartphone pour un prix inférieur à 1000 euro"}
    ]
    @task
    def intent_api(self):
        for sentence in self.sentences:
            url = "/api/intent/?{}".format(urllib.parse.urlencode(sentence))
            self.client.get(url)
