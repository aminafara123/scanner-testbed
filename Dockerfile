# Planted container issues. Never build or run this.
# Outdated base image, runs as root, curl piped to shell.
FROM ubuntu:18.04

RUN apt-get update && apt-get install -y curl python3 python3-pip

RUN curl -sL https://example.com/install.sh | sh

COPY . /app
WORKDIR /app

RUN pip3 install -r requirements.txt

EXPOSE 5000
CMD ["python3", "app.py"]
