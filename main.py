import requests

payload = {'hapikey': 'demo'}
r = requests.get('https://api.hubapi.com/contacts/v1/lists/all/contacts/all', params=payload)
print(r.json)
print(r.headers)
#print(r.text)
#for key, value in r.headers.items():
#    print(key, value)
#print(r.headers)
total_contacts = r.headers.get('Content-Length')
print(total_contacts)
print(r.json)
recent_contacts = requests.get('https://api.hubapi.com/contacts/v1/lists/recently_updated/contacts/recent',
                               params=payload)


