FROM python:alpine3.8

# Define current working directory.
WORKDIR /app

RUN pip3 install -r /app/requirements.txt

CMD python3 /app/app.py

EXPOSE 5000
