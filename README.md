
# layer-kafka-subclient
This layer functions as a client for the [kafka-subscriber](https://github.com/IBCNServices/layer-kafka-subscriber) layer. It allows you to subscribe and unsubscribe to Apache Kafka topics. By specifying an endpoint the Kafka messages will be send via HTTP Post. 

# Usage

Add this layer to layer.yaml
```
includes: ['layer: kafka-subclient']
```

This layer provides three configuration parameters:
1. topics: ; seperated list of topics to subscribe to. Can be left empty, the subscriber will remember your endpoint but not send any messages. (Ex. topic1;topic2) 
2. endpoint: Endpoint to which the subscriber will send the Kafka messages. (Ex. 172.28.0.28/log)
3. subscriber: IP adress of the kafka-subscriber service.

Subscriptions will be started when the endpoint and subscriber config parameters are filled in.

## Authors

This software was created in the [IBCN research group](https://www.ibcn.intec.ugent.be/) of [Ghent University](http://www.ugent.be/en) in Belgium. This software is used in [Tengu](http://tengu.intec.ugent.be), a project that aims to make experimenting with data frameworks and tools as easy as possible.

 - Sander Borny <sander.borny@intec.ugent.be>
