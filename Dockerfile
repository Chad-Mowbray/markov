FROM python:3.10-alpine

WORKDIR /myapp

COPY . .

CMD ["python", "server.py"]