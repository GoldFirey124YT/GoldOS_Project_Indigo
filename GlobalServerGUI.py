import paho.mqtt.client as mqtt

# Set up the MQTT client
client = mqtt.Client()
client.connect("mqtt.eclipse.org", 1883, 60)

# Define the message handler
def on_message(client, userdata, message):
    print(message.topic, message.payload.decode())

# Set up the message handler
client.on_message = on_message

# Start the MQTT client loop
client.loop_start()

# Subscribe to the message topic
client.subscribe("my/topic")

# Continuously listen for incoming messages
while True:
    pass
