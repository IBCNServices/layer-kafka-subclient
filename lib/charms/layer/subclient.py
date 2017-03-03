import requests
import json
from charmhelpers.core import hookenv

config = hookenv.config()

def subscribe(subscriber, config):
    try:
        headers = {'Content-type': 'application/json'}
        r = requests.put("http://" + subscriber + "/subscribe", data=json.dumps(config), headers=headers)
    except requests.exceptions.RequestException as e:
        hookenv.log(e)

def unsubscribe(subscriber, config):
    try:
        headers = {'Content-type': 'application/json'}
        r = requests.delete("http://" + subscriber + "/unsubscribe", data=json.dumps(config), headers=headers)
    except requests.exceptions.RequestException as e:
        hookenv.log(e)