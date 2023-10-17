from pulsar import Client, ConsumerType

service_url = "pulsar://localhost:6650"  # Replace with your Pulsar service URL
topic_name = "sample-topic"

client = Client(service_url)

consumer = client.subscribe(
    topic_name,
    subscription_name="my-subscription",
    consumer_type=ConsumerType.Exclusive
)

while True:
    msg = consumer.receive()
    try:
        print(f"Received message: {msg.data()}")
        consumer.acknowledge(msg)
    except Exception as e:
        print(f"Error processing message: {str(e)}")

consumer.close()
client.close()
