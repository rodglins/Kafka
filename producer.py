# -*- coding: utf-8 -*-
"""Producer.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SySRggPMaZHJf-Erv9Ai1-0sQC4kzM6U
"""

!pip install confluent_kafka

import sys
import os

from confluent_kafka import Producer

def delivery_callback(err, msg):
    if err:
        print('%% Message failed delivery: %s\n', err)
    else:
        print('%% Message delivered to %s [%d]\n',
                          (msg.topic(), msg.partition()))

def createTopic():
    print("init");

    topic = 'qtqeeXXX-default'
    # XXX senha secreta, crie a sua
    conf = {
        'bootstrap.servers': 'dory-01.srvs.cloudkafka.com:9094,dory-02.srvs.cloudkafka.com:9094,dory-03.srvs.cloudkafka.com:9094',
        'session.timeout.ms': 6000,
        'default.topic.config': {'auto.offset.reset': 'smallest'},
        'security.protocol': 'SASL_SSL',
	'sasl.mechanisms': 'SCRAM-SHA-256',
        'sasl.username': 'qtqeeXXX',
        'sasl.password': 'euoE0gXG4L9wbTbiaN7I9UP-XXX'
    }

    p = Producer(conf)

    try:
        p.produce(topic, "este eh um teste 4 de mensagem utilizando o Kafka", callback=delivery_callback)
    except BufferError as e:
        print('%% Local producer queue is full (%d messages awaiting delivery): try again\n',
                          len(p))
    p.poll(0)

    print('%% Waiting for %d deliveries\n' % len(p))
    p.flush()

createTopic();