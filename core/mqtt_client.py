import paho.mqtt.client as mqtt
import paho.mqtt.enums as cb_ver


def mqtt_on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker")

        # Subscribe to topics when connected
        client.subscribe("topic1")

    else:
        print(f"Failed to connect, return code={rc}")


def mqtt_on_message(client, userdata, msg):
    print(f"Received message: {msg.topic} {str(msg.payload)}")


def start_mqtt_client(client_id, endpoint):

    client = mqtt.Client(cb_ver.CallbackAPIVersion.VERSION1, client_id)
    client.on_connect = mqtt_on_connect
    client.on_message = mqtt_on_message
    
    client.connect(endpoint, 1883)
    client.loop_start()

    new_topic = client_id
    client.publish(new_topic, "Hello, world!")

    print("MQTT Client Connected.")

    return client

