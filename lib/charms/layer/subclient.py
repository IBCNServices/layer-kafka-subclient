import requests
import json
from charmhelpers.core import hookenv
from requests.auth import HTTPBasicAuth

config = hookenv.config()

def subscribe(subscriber, payload):
    try:
        headers = {'Content-type': 'application/json'}
        if config['credentials']:
            credentials = config['credentials'].split(' ')
            r = requests.put("https://" + subscriber + "/subscribe",
                             data=json.dumps(payload),
                             headers=headers,
                             auth=HTTPBasicAuth(credentials[0], credentials[1]))
        else:
            r = requests.put("http://" + subscriber + "/subscribe",
                             data=json.dumps(payload),
                             headers=headers)
    except requests.exceptions.RequestException as e:
        hookenv.log(e)

def unsubscribe(subscriber, payload):
    try:
        headers = {'Content-type': 'application/json'}
        if config['credentials']:
            credentials = config['credentials'].split(' ')
            r = requests.delete("http://" + subscriber + "/unsubscribe", 
                                data=json.dumps(payload), 
                                headers=headers,
                                auth=HTTPBasicAuth(credentials[0], credentials[1]))
        else:
            r = requests.delete("http://" + subscriber + "/unsubscribe",
                                data=json.dumps(payload), 
                                headers=headers)
    except requests.exceptions.RequestException as e:
        hookenv.log(e)