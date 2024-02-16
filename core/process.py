import websocket
import warnings


# Suppress all warnings
warnings.filterwarnings("ignore")


if __name__ == "__main__":

    user_data = setup()

    #user_data = {"topic": topic,
    #            "username": name, 
    #            "visibility": visibility, 
    #            "mqtt_endpoint": mqtt_enpoint, 
    #            "server_endpoint": server_endpoint}

    start_mqtt_client(user_data["username"], user_data["mqtt_enpoint"])
    start_ws_client(user_data["server_endpoint"])

    while True:
            
        detect_aps()

        fingerprint = ""
        for index, row in detected_aps.iterrows():
            bssid = row['bssid'].upper()
            signal_strength = row['dBm_signal']
            fingerprint += f"{bssid}, {signal_strength}"
            
            # Check if it's not the last row
            if index < len(detected_aps) - 1:
                fingerprint += "\n"

        #send scan results to server 
        ws.send(fingerprint)

        #upon server response, send results to mqtt broker. 

    
