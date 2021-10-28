FROM python:3.9.7

WORKDIR .

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5555

COPY . .
CMD ["python", "-u", "app/udaconnect/services.py"]