import grpc
import logging
import location_pb2
import location_pb2_grpc
import time
from concurrent import futures
from json import dumps
from kafka import KafkaProducer


producer = KafkaProducer(bootstrap_servers=['my-cluster-kafka-bootstrap.kafka.svc.cluster.local:9092'],
                         value_serializer=lambda v:
                         dumps(v).encode('utf-8'),api_version=(0, 10, 2))


class LocationService(location_pb2_grpc.LocationServiceServicer):
    def Create(self, request, context):
        print("received")
        location = {
            "person_id": request.person_id,
            "latitude": request.latitude,
            "longitude": request.longitude
        }
        producer.send("location", location)
        producer.flush()
        return location_pb2.LocationMessage(**location)


logging.basicConfig()

# Initializes the gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
location_pb2_grpc.add_LocationServiceServicer_to_server(LocationService(), server)

print("Server starting on port 5555..")
server.add_insecure_port("[::]:5555")
server.start()

# Keep thread alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
