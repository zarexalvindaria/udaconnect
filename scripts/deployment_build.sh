# persons api
 docker build -t persons .
 docker run -d -p 50051:50051 persons
 docker tag persons zarexalvindaria/persons:latest
 docker push zarexalvindaria/persons:latest

# persons api
 docker build -t connection .
 docker run -d -p 50052:50052 connection
 docker tag connection zarexalvindaria/connection:latest
 docker push zarexalvindaria/connection:latest


# Example persons data
insert into public.person (id, first_name, last_name, company_name) values (2, 'Aljur', 'Abrenica', 'Tender Juicy');
insert into public.person (id, first_name, last_name, company_name) values (3, 'Kylie', 'Padilla', 'Momzillas');
insert into public.person (id, first_name, last_name, company_name) values (4, 'AJ', 'Raval', 'Chick Fillet');

-----

# running protoc
python -m grpc_tools.protoc -I./ --python_out=./ --grpc_python_out=./ location.proto

# location producer
 docker build -t location-producer .
 # docker run -d -p 5555:5555 location-producer --for testing
 docker tag location-producer zarexalvindaria/location-producer:latest
 docker push zarexalvindaria/location-producer:latest

#Installing and activating kafka
1. Create kafka namespace
kubectl create namespace kafka

2. Apply Strimzi install files
kubectl create -f 'https://strimzi.io/install/latest?namespace=kafka' -n kafka

3. Provision Kafka cluster
# Apply the `Kafka` Cluster CR file
kubectl apply -f https://strimzi.io/examples/latest/kafka/kafka-persistent-single.yaml -n kafka

#We now need to wait while Kubernetes starts the required pods, services and so on:
kubectl wait kafka/my-cluster --for=condition=Ready --timeout=300s -n kafka

4. Send and receive messages
# create a producer
kubectl -n kafka run kafka-producer -ti --image=quay.io/strimzi/kafka:0.26.0-kafka-3.0.0 --rm=true --restart=Never -- bin/kafka-console-producer.sh --broker-list my-cluster-kafka-bootstrap:9092 --topic location

# create a consumer
kubectl -n kafka run kafka-consumer -ti --image=quay.io/strimzi/kafka:0.26.0-kafka-3.0.0 --rm=true --restart=Never -- bin/kafka-console-consumer.sh --bootstrap-server my-cluster-kafka-bootstrap:9092 --topic location --from-beginning


# location consumer
 docker build -t location-consumer .
 #docker run -d -p 6666:6666 location-consumer
 docker tag location-consumer zarexalvindaria/location-consumer:latest
 docker push zarexalvindaria/location-consumer:latest


 # inspect table values (postgres-5f676c995d-sdlnd is the pod id)
 kubectl exec -it postgres-5f676c995d-sdlnd -- psql -d geoconnections -U ct_admin -c '\x' -c 'SELECT * FROM public.location;'
 kubectl exec -it postgres-5f676c995d-sdlnd -- psql -d geoconnections -U ct_admin -c '\x' -c 'SELECT * FROM public.person;'