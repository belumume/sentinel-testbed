dockerfile
FROM ubuntu:16.04

# BAD: Running as root
USER root

# BAD: Not pinning package versions
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    curl \
    wget

# BAD: Hardcoded secrets in Dockerfile
ENV API_KEY=sk_test_1234567890abcdef
ENV DB_PASSWORD=supersecret123

# BAD: Copying everything including sensitive files
COPY . /app

WORKDIR /app

# BAD: Installing packages as root
RUN pip3 install -r requirements.txt

# BAD: Exposing unnecessary ports
EXPOSE 22 3306 5432 6379

CMD ["python3", "app.py"]
