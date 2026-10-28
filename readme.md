# Python Kafka Messaging with Docker

## Overview

A beginner-friendly messaging project using Apache Kafka,
Docker Compose, and Python.

The Python producer sends JSON messages to a Kafka topic.
The Python consumer reads and processes those messages.

## Architecture

Python Producer -> Kafka Topic -> Python Consumer

## Technologies

- Python
- Apache Kafka
- Docker
- Docker Compose
- kafka-python

## Features

- Kafka runs in a Docker container.
- Python producer publishes JSON messages.
- Python consumer reads messages from Kafka.
- Consumer handles both JSON and plain-text messages.

## Prerequisites

- Python
- Docker Desktop
- Docker Compose

## Setup

Install the Python dependency:

    python -m pip install -r requirements.txt

Start Kafka:

    docker compose up -d

Run the consumer in Terminal 1:

    python consumer.py

Run the producer in Terminal 2:

    python producer.py

## Stop Kafka

    docker compose down

## Learning Outcomes

- Docker container management
- Kafka topics, producers, and consumers
- Python messaging
- JSON serialization and deserialization