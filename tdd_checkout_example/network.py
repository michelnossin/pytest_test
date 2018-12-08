import requests


class Network:
    def __init__(self):
        pass

    def get_url(self, url):
        return requests.get(url)
