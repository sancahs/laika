FROM python:3.14-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
            python3-virtualenv \
            python3-dev && \
    mkdir -p /etc/laika/laika

COPY laika/ /etc/laika/laika
COPY pyproject.toml /etc/laika

RUN pip3 install -U \
        pip \
        setuptools \
        wheel \
        uv && \
    cd /etc/laika && \
    uv sync

WORKDIR /etc/laika/laika
RUN useradd laika
USER laika

CMD ["uv", "--no-cache", "run", "fastapi", "run", "--port", "8080"]
EXPOSE 8080
