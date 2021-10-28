from __future__ import annotations
from typing import Dict
import json
from kafka import KafkaConsumer
import psycopg2
import logging
from config import DB_USERNAME, DB_HOST, DB_NAME, DB_PORT, DB_PASSWORD

TOPIC_NAME = 'location'
messages = KafkaConsumer(TOPIC_NAME, bootstrap_servers=['my-cluster-kafka-bootstrap.kafka.svc.cluster.local:9092'])


def _add_to_location(location: Dict):
    session = psycopg2.connect(dbname=DB_NAME, port=DB_PORT, user=DB_USERNAME, password=DB_PASSWORD, host=DB_HOST)
    cursor = session.cursor()
    cursor.execute(
        'INSERT INTO location (person_id, coordinate) VALUES ({}, ST_Point({}, {}));'.format(
            int(location["person_id"]), float(location["latitude"]), float(location["longitude"])))
    session.commit()
    cursor.close()
    session.close()

    print("Location added to the database!")
    return location


def consume_message():
    for message in messages:
        location = json.loads(message.value.decode("utf-8"))
        _add_to_location(location)


logging.basicConfig()
consume_message()