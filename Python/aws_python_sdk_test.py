# Import SDK packages
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

# Custom MQTT message callback
def customCallback(client, userdata, message):
    print("Received a new message: ")
    print(message.payload)
    print("from topic: ")
    print(message.topic)
    print("--------------\n\n")


# For certificate based connection
myMQTTClient = AWSIoTMQTTClient("client_123")

myMQTTClient.configureEndpoint("a3r2gm16zr92x7-ats.iot.us-west-2.amazonaws.com", 8883)

myMQTTClient.configureCredentials(".\\root-CA.crt", ".\\f10794e58b-private.pem.key", ".\\f10794e58b-certificate.pem.crt")
myMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
myMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
myMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
myMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec

myMQTTClient.connect()
myMQTTClient.subscribe("room1", 1, customCallback)
myMQTTClient.publish("room1", "AWS_SDK_test_msg", 0)
