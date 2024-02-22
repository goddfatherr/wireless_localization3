import websocket
import threading
import warnings
import time
import os

from  platform_dependent import find_apsV3
import mqtt_client
import ws_client
import setup

# Suppress all warnings
warnings.filterwarnings("ignore")



if __name__ == "__main__":
    global mqtt_client_conn

    # ctrl + c does not kill ws.run_forever(). 
    # use the PID to kill it instead
    # on powershell:
    #taskkill /F /PID <PID>
    print(f"Process ID (PID): {os.getpid()}")

    user_data = setup.setup()

    #user_data = {"topic": topic,
    #            "username": name, 
    #            "visibility": visibility, 
    #            "mqtt_endpoint": mqtt_enpoint, 
    #            "server_endpoint": server_endpoint}

    #print(user_data)

    # start mqtt client
    server_endpoint = user_data["mqtt_endpoint"]
    username = user_data["username"]
    ws_client.topic = username
    ws_client.mqtt_client_conn = mqtt_client.start_mqtt_client(username, server_endpoint)

    # start ws client
    server_endpoint = user_data["server_endpoint"]
    wss_client_conn = ws_client.start_ws_client(server_endpoint)

    # run ws client indefinetly in another thread
    thread = threading.Thread( target = ws_client.run_ws_indefinte, args = (wss_client_conn,))
    thread.start()

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
        
        # format fingerprint appropirately
        fingerprint = fingerprint.replace(':', '')
        print(fingerprint,"\n\n")

        #send scan results to server 
        wss_client_conn.send(fingerprint)

        time.sleep(10) 

    
