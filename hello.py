from flask import Flask
import requests

app = Flask(__name__)

apikey = "demo"

@app.route("/")
def hello():
    payload = {'hapikey' : 'demo'}
    r = requests.get('https://api.hubapi.com/contacts/v1/lists/all/contacts/all', params=payload)
    total_contacts = r.headers.get('Content-Length')
    print(total_contacts)
    display_text = "Total Contacts in System %s" % total_contacts
    return display_text

@app.route("/recent")
def recent_contacts():
    payload = {'hapikey' : 'demo'}
    recent_contacts = requests.get('https://api.hubapi.com/contacts/v1/lists/recently_updated/contacts/recent',
                                   params=payload)
    display_text = recent_contacts.text
    return display_text