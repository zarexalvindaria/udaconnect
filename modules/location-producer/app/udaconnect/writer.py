import grpc
import location_pb2
import location_pb2_grpc

print("Sending sample payload...")


channel = grpc.insecure_channel("localhost:30020")
stub = location_pb2_grpc.LocationServiceStub(channel)

location = location_pb2.LocationMessage(
    person_id=1,
    latitude=14.67202413207315,
    longitude=121.03856982696303
)

response = stub.Create(location)
