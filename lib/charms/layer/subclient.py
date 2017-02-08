import requests
import json
from charmhelpers.core import hookenv

config = hookenv.config()


def subscribe(subscriber, config):
	headers = {'Content-type': 'application/json'}
	r = requests.put("http://" + subscriber + "/subscribe", data=json.dumps(config), headers=headers)

def unsubscribe(subscriber, config):
	headers = {'Content-type': 'application/json'}
	hookenv.log(json.dumps(config))
	r = requests.delete("http://" + subscriber + "/unsubscribe", data=json.dumps(config), headers=headers)