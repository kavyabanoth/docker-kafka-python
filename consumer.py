from kafka import KafkaConsumer
import json

def deserialize_message(value):
    try:
        return json.loads(value.decode("utf-8"))
    except (json.JSONDecodeError, UnicodeDecodeError):
        return value.decode("utf-8", errors="replace")

consumer = KafkaConsumer(
    "test-topic",
    bootstrap_servers=["kafka:29092"],
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    value_deserializer=deserialize_message
)

print("Waiting for messages... Press Ctrl+C to stop.")

try:
    for message in consumer:
        print(f"Received: {message.value}")

except KeyboardInterrupt:
    print("\nConsumer stopped.")

finally:
    consumer.close()