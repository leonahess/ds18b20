FROM python:alpine

ADD smarthome_ds18b20.py .
ADD config.py .
ADD requirements.txt .
ADD app ./app

WORKDIR .

RUN pip3 install -r requirements.txt

CMD ["python3", "smarthome_ds18b20.py"]
