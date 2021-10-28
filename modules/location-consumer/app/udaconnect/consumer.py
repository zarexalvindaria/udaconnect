from __future__ import annotations
from typing import Dict
import json
from kafka import KafkaConsumer
import os
import psycopg2
import logging

DB_USERNAME = os.environ["DB_USERNAME"]
DB_PASSWORD = os.environ["DB_PASSWORD"]
DB_HOST = os.environ["DB_HOST"]
DB_PORT = os.environ["DB_PORT"]
DB_NAME = os.environ["DB_NAME"]

TOPIC_NAME = 'location'
messages = KafkaConsumer(TOPIC_NAME, bootstrap_servers=['my-cluster-kafka-bootstrap.kafka.svc.cluster.local:9092'])


def _add_to_location(location: Dict):
    session = psycopg2.connect(dbname=DB_NAME, port=DB_PORT, user=DB_USERNAME, password=DB_PASSWORD, host=DB_HOST)

    # SQL Query
    query = 'INSERT INTO location (person_id, coordinate) VALUES ({}, ST_Point({}, {}));'.format(
        int(location["person_id"]), float(location["latitude"]), float(location["longitude"]))

    cursor = session.cursor()
    cursor.execute(query)
    session.commit()
    cursor.close()
    session.close()  # Close the session

    print("Message added to the database!")
    return location


def consume_message():
    for message in messages:
        loc = json.loads(message.value.decode("utf-8"))
        _add_to_location(loc)


logging.basicConfig()
consume_message()
