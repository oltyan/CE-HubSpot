from flask import Flask
import requests

app = Flask(__name__)

apikey = "demo"

@app.route("/")
def hello():
    payload = {'hapikey' : 'demo'}
    r = requests.get('https://api.hubapi.com/contacts/v1/lists/all/contacts/all', params=payload)
    prepared = print(r.json)
    return r.text

def hubspot():
    payload = {'hapikey' : 'demo'}
    r = requests.get('https://api.hubapi.com/contacts/v1/lists/all/contacts/all', params=payload)
    print(r)