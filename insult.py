import requests
import json

def get_insult():
    resp = requests.get(r"https://evilinsult.com/generate_insult.php?lang=en&type=json")

    if resp.status_code == 200:
        return json.loads(resp.text)['insult']
    else:
        return "Well I just don't like you that much"


def get_trump():
    resp = requests.get(r"https://api.tronalddump.io/random/quote")

    if resp.status_code == 200:
        return json.loads(resp.text)['value']
    else:
        return "We're staying in Syria for the oil'"