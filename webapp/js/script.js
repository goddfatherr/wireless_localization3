const brokerAddress = "ws://172.22.206.85";
const username = "";
const password = "";

var timeoutId = 0;
var previous_sub_topic = "";

const options = {
  clientId: 'web-client',
  username: username,
  password: password,
  reconnectPeriod: 5000, 
  cleanSession: true,
  port: 8083,
  path: '/mqtt'
};

const client = mqtt.connect(brokerAddress, options);

const onConnect = () => {
  console.log("Connected to MQTT broker!");
};

const onError = (error) => {
  console.error("MQTT error:", error);
};

const onMessage = (topic, message) => {
  console.log(`Received message on topic ${topic}: ${message.toString()}`);
  responseArea.textContent = message.toString();
  responseArea.classList.add("show");
  clearTimeout(timeoutId); 
};

const onTimeout = () => {
  console.log("No message received, User Offline");
  responseArea.textContent = "User Offline";
  responseArea.classList.add("show");
};

const responseArea = document.getElementById("response-area");

const sendBtn = document.getElementById("send-btn");

responseArea.textContent = "";

sendBtn.addEventListener("click", () => {
  const topic = document.querySelector("input[type='text']").value;

  //If input is empty, fill it with the last username
  //console.log(topic, previous_sub_topic);
  if (topic == "") {
    document.querySelector("input[type='text']").value = previous_sub_topic; 
    return;
  }
  //If subscribed to location update of current user, nothing to be done
  if (previous_sub_topic == topic) {
    return;
  }

  //If subscribed to a different user location update, unsubscribe first
  console.log(previous_sub_topic);
  if (previous_sub_topic != "") {
    client.unsubscribe(previous_sub_topic, (err) => {
        if (err) {
          console.error("Error unsubscribing:", err);
          return;
        }
        console.log(`Unsubscribed to previous topic: ${previous_sub_topic}`);
      });
  }

  //Subscribe to recieve location update of new user. 
  client.subscribe(topic, (err) => {
    if (err) {
      console.error("Error subscribing:", err);
      return;
    }
    console.log(`Subscribed to topic: ${topic}`);
    responseArea.textContent = "Locating...";
    responseArea.classList.add("show");

    previous_sub_topic = topic;

    timeoutId = setTimeout(onTimeout, 10000); // Set timeout for 10 seconds
  });

  //previous_sub_topic = topic;
});


// Connect to the broker when page loads
client.on("connect", onConnect);
client.on("error", onError);
client.on("message", onMessage);
