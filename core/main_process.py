import websocket
import warnings
import time

import mqtt_client
import ws_client
import setup
from  platform_dependent import find_apsV3


# Suppress all warnings
warnings.filterwarnings("ignore")


if __name__ == "__main__":

    user_data = setup.setup()

    #user_data = {"topic": topic,
    #            "username": name, 
    #            "visibility": visibility, 
    #            "mqtt_endpoint": mqtt_enpoint, 
    #            "server_endpoint": server_endpoint}

    #print(user_data)

    mqtt_client = mqtt_client.start_mqtt_client(user_data["username"], user_data["mqtt_endpoint"])
    #ws_client.start_ws_client(user_data["server_endpoint"])

    while True:
            
        find_apsV3.detect_aps()

        fingerprint = ""
        for index, row in find_apsV3.detected_aps.iterrows():
            bssid = row['bssid'].upper()
            signal_strength = row['dBm_signal']
            fingerprint += f"{bssid}, {signal_strength}"
            
            # Check if it's not the last row
            if index < len(find_apsV3.detected_aps) - 1:
                fingerprint += "\n"

        print(fingerprint,"\n\n")

        #send scan results to server 
        #ws.send(fingerprint)

        time.sleep(10) 

    
