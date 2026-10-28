from kafka import KafkaProducer
import json
import time

producer = KafkaProducer(
    bootstrap_servers=["kafka:29092"],
    value_serializer=lambda value: json.dumps(value).encode("utf-8")
)

try:
    for i in range(1, 6):
        message = {
            "id": i,
            "message": f"Hello from Python! Message {i}"
        }

        producer.send("test-topic", value=message)
        print(f"Sent: {message}")

        time.sleep(1)

    producer.flush()

finally:
    producer.close()