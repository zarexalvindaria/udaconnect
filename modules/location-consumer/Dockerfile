FROM python:3.9.7

WORKDIR .

#RUN apk add --no-cache gcc musl-dev linux-headers geos libc-dev postgresql-dev
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 6666

COPY . .
#CMD ["flask", "run", "--host", "0.0.0.0"]
CMD ["python", "-u", "app/udaconnect/consumer.py"]
#CMD ["flask", "run", "--host", "0.0.0.0", "python", "-u", "app/udaconnect/consumer.py"]