# Python Kafka Messaging with Docker

## Overview

A Python messaging application using Apache Kafka, Docker, Docker Compose, and AWS EC2.

The Python producer sends JSON messages to a Kafka topic. The Python consumer reads and processes those messages.

## Architecture

Python Producer -> Kafka Topic (test-topic) -> Python Consumer

All application services communicate through Docker Compose's internal network.

## Technologies

- Python
- Apache Kafka
- Docker
- Docker Compose
- kafka-python
- AWS EC2
- Linux
- GitHub Actions

## Features

- Publishes JSON messages using a Python producer.
- Transfers messages through an Apache Kafka topic.
- Consumes and deserializes JSON messages.
- Runs Kafka, producer, and consumer using Docker Compose.
- Uses a Docker volume for Kafka data persistence.
- Deploys the application on AWS EC2.

## Project Structure

- Dockerfile
- docker-compose.yml
- producer.py
- consumer.py
- requirements.txt
- .github/workflows/python-ci.yml
- readme.md

## Prerequisites

- Git
- Docker Engine
- Docker Compose
- An AWS account for cloud deployment

## Run the Application

Clone the repository:

    git clone https://github.com/kavyabanoth/docker-kafka-python.git
    cd docker-kafka-python

Build the application images:

    docker compose build

Start the services:

    docker compose up -d

Check the services:

    docker compose ps

View producer logs:

    docker compose logs producer

View consumer logs:

    docker compose logs consumer

The producer sends five JSON messages to the test-topic Kafka topic. The consumer receives and prints the messages.

Stop the services:

    docker compose down

## AWS EC2 Deployment

The application was tested on an Amazon Linux 2023 EC2 instance.

Deployment workflow:

1. Launch an EC2 Linux instance.
2. Connect using SSH.
3. Install Docker, Docker Compose, and Git.
4. Clone the project repository.
5. Build the application images.
6. Start the services with Docker Compose.
7. Inspect producer and consumer logs.

Verification commands:

    docker compose ps
    docker compose logs --tail=50 producer
    docker compose logs --tail=50 consumer

In the successful test, the producer sent five messages and the consumer received all five.

## Security

- Kafka communication uses the internal Docker network.
- Do not expose Kafka's unauthenticated port publicly.
- Restrict SSH access to trusted IP addresses.
- Never commit AWS private keys, passwords, or API tokens.

## Learning Outcomes

- Containerizing Python applications.
- Running multiple containers with Docker Compose.
- Understanding Kafka producers, consumers, and topics.
- Working with JSON serialization and deserialization.
- Deploying containerized applications on AWS EC2.
- Troubleshooting Docker networking.

## Future Improvements

- Publish application images to a container registry.
- Extend GitHub Actions for automated image builds.
- Add monitoring and logging.
- Learn Terraform for infrastructure provisioning.
- Explore Kubernetes fundamentals.