import paho.mqtt.client as mqtt

def mqtt_on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker")

        # Subscribe to topics when connected
        client.subscribe("topic1")

    else:
        print(f"Failed to connect, return code={rc}")


def mqtt_on_message(client, userdata, msg):
    print(f"Received message: {msg.topic} {str(msg.payload)}")


def start_mqtt_client(username, endpoint):
    client = mqtt.Client()
    client.mqtt_on_connect = on_connect
    client.mqTT_on_message = on_message
    
    client.connect("mqtt.example.com", 1883)
    client.loop_start()

    new_topic = username
    client.publish(new_topic, "Hello, world!")
