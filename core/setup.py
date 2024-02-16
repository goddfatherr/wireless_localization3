
def setup():
    user_data = []

    while True:
        name = input("Please enter your name (single word without spaces): ")
        if ' ' in name:
            print("Error: Spaces detected")
        else:
            print("Thank you,", name + "!")
            break

    
    while True:
        visibility = input("Do you want to be visible online? Y/n: ")
        if visibility !='Y':
            visibility = "offline"
        else:
            visibility = "online"    
    
    topic = "nodes/" + name

    #Admin
    mqtt_endpoint = input("Enter Broker Endpoint: ")
    server_endpoint = input("Enter Server Endpoint: ")

    user_data = {"username": name, 
                "visibility": visibility, 
                "topic": topic,
                "mqtt_endpoint": mqtt_enpoint, 
                "server_endpoint": server_endpoint}

    

    return user_data