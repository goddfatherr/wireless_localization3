from datetime import datetime
import websocket
import warnings
import rel

mqtt_client_conn = ""
topic = ""
# Suppress all warnings
warnings.filterwarnings("ignore")

def ws_on_message(ws, message):
    global mqtt_client_conn
    global topic

    print(f"Received message: {message}")

    #publish response to mqttt broker
    payload = f"Last seen place: {message}\nLast seen time: {datetime.now()}"

    mqtt_client_conn.publish(topic, payload) 
   
def ws_on_error(ws, error):
    print(f"Error occurred: {error}")

def ws_on_close(ws, close_status_code, close_msg):
    print(f"Connection closed with status code {close_status_code}: {close_msg}")

def ws_on_open(ws):
    print("Opened Websocket connection")

def start_ws_client(endpoint):
    websocket.enableTrace(False)

    ws = websocket.WebSocketApp('ws://' + endpoint + ':80/ws',
                                on_open=ws_on_open,
                                on_message=ws_on_message,
                                on_error=ws_on_error,
                                on_close=ws_on_close)
    return ws

def run_ws_indefinte(ws):

    ws.run_forever()

    #these lines only works in main thread
    #ws.run_forever(dispatcher=rel, reconnect=5) 
    #rel.signal(2, rel.abort) 
    #rel.dispatch()  

