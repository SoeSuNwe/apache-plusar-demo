from pulsar import Client

service_url = "pulsar://localhost:6650"  # Replace with your Pulsar service URL
topic_name = "sample-topic"

client = Client(service_url)

producer = client.create_producer(topic_name)

for i in range(10):
    message = f"Message {i}"
    producer.send(message.encode('utf-8'))
    print(f"Sent: {message}")

producer.close()
client.close()
