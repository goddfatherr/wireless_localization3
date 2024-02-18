
def setup():
    user_data = []

    while True:
        #need to add logic to make sure username does not already exist. 

        name = input("Please enter your username (single word): ")
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
        
        break
    topic = "nodes/" + name

    #Admin
    mqtt_endpoint = input("Enter Broker Endpoint: ")
    server_endpoint = input("Enter Server Endpoint: ")

    user_data = {"username": name, 
                "visibility": visibility, 
                "topic": topic,
                "mqtt_endpoint": mqtt_endpoint, 
                "server_endpoint": server_endpoint}

    

    return user_data