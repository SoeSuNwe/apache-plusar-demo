from pulsar import Client, ConsumerType

service_url = "pulsar://localhost:6650"
namespace_tenant_a = "tenant-a/ns-1"
namespace_tenant_b = "tenant-b/ns-1"

topic_a_name = "sample-topic-A"
topic_b_name = "sample-topic-B"

client = Client(service_url)

consumer_tenant_a = client.subscribe(
    f"persistent://{namespace_tenant_a}/{topic_a_name}",
    subscription_name="my-subscription",
    consumer_type=ConsumerType.Exclusive
)

consumer_tenant_b = client.subscribe(
    f"persistent://{namespace_tenant_b}/{topic_b_name}",
    subscription_name="my-subscription",
    consumer_type=ConsumerType.Exclusive
)

# Attempt to read messages from Tenant A's namespace
for _ in range(5):
    msg = consumer_tenant_a.receive()
    print(f"Tenant A received: {msg.data()}")
    consumer_tenant_a.acknowledge(msg)

# Attempt to read messages from Tenant B's namespace
for _ in range(5):
    msg = consumer_tenant_b.receive()
    print(f"Tenant B received: {msg.data()}")
    consumer_tenant_b.acknowledge(msg)

consumer_tenant_a.close()
consumer_tenant_b.close()
client.close()
