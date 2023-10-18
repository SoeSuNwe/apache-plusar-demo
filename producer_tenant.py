from pulsar import Client

service_url = "pulsar://localhost:6650"  # Replace with your Pulsar service URL
topic_a_name = "sample-topic-A"
topic_b_name = "sample-topic-B"

#replace namespace_tenant
namespace_tenant_a = "tenant-a/ns-1"
namespace_tenant_b = "tenant-b/ns-1"

client = Client(service_url)

# Create a producer for each namespace

producer_tenant_a = client.create_producer(f"persistent://{namespace_tenant_a}/{topic_a_name}")
producer_tenant_b = client.create_producer(f"persistent://{namespace_tenant_b}/{topic_b_name}")

# Send messages from Tenant A
for i in range(5):
    producer_tenant_a.send(f"Message from Tenant A {i}".encode('utf-8'))

# Send messages from Tenant B
for i in range(5):
    producer_tenant_b.send(f"Message from Tenant B {i}".encode('utf-8'))

producer_tenant_a.close()
producer_tenant_b.close()
client.close()
