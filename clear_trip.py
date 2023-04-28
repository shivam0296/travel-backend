import time
from paho.mqtt import client as mqtt_client



class MqttClear:

    def __init__(self):
        self.broker = 'broker.hivemq.com' 
        self.topic = 'travel-buddy/{0}/{1}'.format('any'.lower().replace(' ','-'), 'any'.lower().replace(' ','-'))
        self.client_id = 'tourist_1' #from app
        self.client_name = 'Tourist 1' #from app

    def connect_mqtt(self):
        def on_connect(client, userdata, flags, rc):
            if rc == 0:
                print("Connected to MQTT Broker!")
            else:
                print("Failed to connect, return code %d\n", rc)

        client = mqtt_client.Client(self.client_id)
        client.on_connect = on_connect
        client.connect(self.broker)
        return client


    def publish(self, client):
        
        result = client.publish(self.topic,'',retain = True)
        status = result[0]
        if status == 0:
            print('Timeout! Trip Cleared Successfully!')
            return True
        else:
            print('Trip not published!')
            return False

    def run(self):
        client = self.connect_mqtt()
        time.sleep(1)
        client.loop_start()
        success = self.publish(client)
        client.loop_stop()
        client.disconnect()
        return success
