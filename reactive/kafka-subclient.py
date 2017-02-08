from charms.reactive import when, when_not, hook
from charms.reactive import set_state, remove_state
from charmhelpers.core import hookenv
from charmhelpers.core.hookenv import status_set
from charmhelpers.contrib.python.packages import pip_install

from charms.layer.subclient import subscribe, unsubscribe

config = hookenv.config()

@when_not('subclient.installed')
def install():
    hookenv.log("Installing kafka-subclient")
    pip_install('requests')
    set_state('subclient.installed')

@when('config.changed.topics', 'subclient.installed')
def config_changed_topics():
    start()

@when('config.changed.endpoint', 'subclient.installed')
def config_changed_endpoint():
    if config['endpoint'] != "":
        start()

@when('config.changed.subscriber', 'subclient.installed')
def config_changed_subscriber():
    if config['subscriber'] != "":
        start()

def start():
    if config['endpoint'] != "" and config['subscriber'] != "":
        topics = config['topics'].split(' ')
        config_dict = {
            'topics': topics,
            'endpoint': config['endpoint']
        }
        subscribe(config['subscriber'], config_dict)

@hook('stop')
def stop():
    if config['endpoint'] != "" and config['subscriber'] != "":
        hookenv.log('Calling unsubscribe')
        config_dict = {
            'endpoint': config['endpoint']
        }
        unsubscribe(config['subscriber'], config_dict)
