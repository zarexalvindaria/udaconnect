import grpc
import location_pb2
import location_pb2_grpc

print("Sending sample payload...")


channel = grpc.insecure_channel("localhost:30020")
stub = location_pb2_grpc.LocationServiceStub(channel)


# Update this with  payload
location = location_pb2.LocationMessage(

    # id int = 4, -- delete since auto generated
    person_id=3,
    latitude=14.67202413207315,
    longitude=121.03856982696303
)

response = stub.Create(location)


"""
@api.route("/locations")
@api.route("/locations/<location_id>")
@api.param("location_id", "Unique ID for a given Location", _in="query")
class LocationResource(Resource):
    def post(self):
        print("Sending payload...")
        location = location_pb2.LocationMessage(
            request.get_json()
        )
        response = stub.Create(location)
        return response
"""