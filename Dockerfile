
FROM ubuntu:16.04


USER root


RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    curl \
    wget


ENV API_KEY=sk_test_1234567890abcdef
ENV DB_PASSWORD=supersecret123


COPY . /app

WORKDIR /app


RUN pip3 install -r requirements.txt


EXPOSE 22 3306 5432 6379

CMD ["python3", "app.py"]
