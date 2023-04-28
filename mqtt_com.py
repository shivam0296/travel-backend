import time
from paho.mqtt import client as mqtt_client


class AddTrip:

    def __init__(self, client_id, client_name, source_loc, destination_loc):
        self.client_name = client_name
        self.client_id = client_id
        self.source_loc = source_loc
        self.destination_loc =  destination_loc
        self.broker = 'broker.hivemq.com' 
        #topic = "travel-buddy/iu-sample-gates/chicago-downtown" #from app
        self.topic = 'travel-buddy/{0}/{1}'.format(source_loc.lower().replace(' ','-'), destination_loc.lower().replace(' ','-'))

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

        msg = f"""
        Created By: {self.client_name}
        From: {self.source_loc}
        To: {self.destination_loc}
        count: {1}
        """
        result = client.publish(self.topic, msg, retain = True)
        status = result[0]
        if status == 0:
            print(msg)
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


class SearchTour:

    def __init__(self):

        self.broker = 'broker.hivemq.com' 
        self.fav_locs = ['IU Sample Gates','Chicago Downtown','Smoky Mountains', 'Uttar Pradesh']
        #generate all (source,dest) combinations.
        self.all_combs = []
        for s in self.fav_locs:
            for d in self.fav_locs:
                if s!=d:
                    self.all_combs.append((s,d))
        self.topics = ['travel-buddy/{0}/{1}'.format(s.lower().replace(' ','-'), d.lower().replace(' ','-')) for s,d in self.all_combs]
        self.client_id = '' #from app
        self.client_name = 'Tourist 3' #from app
        self.trips_queue = [] #will store list of tuples. Each tuple is a trip.

    def connect_mqtt(self) -> mqtt_client:
        def on_connect(client, userdata, flags, rc):
            if rc == 0:
                print("Connected to MQTT Broker!")
            else:
                print("Failed to connect, return code %d\n", rc)

        client = mqtt_client.Client(self.client_id)
        client.on_connect = on_connect
        client.connect(self.broker)
        return client


    def subscribe(self, client: mqtt_client):
        def on_message(client, userdata, msg):
            #print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
            print(msg.payload.decode())
            actual_msg = msg.payload.decode().split('\n')
            cname = actual_msg[1].split(':')[1].strip()
            src = actual_msg[2].split(':')[1].strip()
            dest = actual_msg[3].split(':')[1].strip()
            cnt = int(actual_msg[4].split(':')[1].strip())
            self.trips_queue.append((cname, src, dest, cnt))

        
        [client.subscribe(t) for t in self.topics]
        client.on_message = on_message


    def run(self):    
    
        client = self.connect_mqtt()
        time.sleep(1)
        client.loop_start()
        self.subscribe(client)
        time.sleep(4) #timer to look for all the trips
        [client.unsubscribe(t) for t in self.topics]
        client.loop_stop()
        client.disconnect()
        return self.trips_queue
    
class SearchTrip:

    def __init__(self, source):
        self.broker = 'broker.hivemq.com'
        self.source_loc = source #from app #destination loc not required.
        self.topic = 'travel-buddy/{0}/+'.format(self.source_loc.lower().replace(' ','-'))
        self.client_id = 'id' #from app
        self.client_name = 'name' #from app
        self.trips_queue = [] #will store list of tuples. Each tuple is a trip.

    def connect_mqtt(self) -> mqtt_client:
        def on_connect(client, userdata, flags, rc):
            if rc == 0:
                print("Connected to MQTT Broker!")
            else:
                print("Failed to connect, return code %d\n", rc)

        client = mqtt_client.Client(self.client_id)
        client.on_connect = on_connect
        client.connect(self.broker)
        return client

    def subscribe(self,client: mqtt_client):
        def on_message(client, userdata, msg):
            #print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
            print(msg.payload.decode())
            actual_msg = msg.payload.decode().split('\n')
            cname = actual_msg[1].split(':')[1].strip()
            src = actual_msg[2].split(':')[1].strip()
            dest = actual_msg[3].split(':')[1].strip()
            cnt = int(actual_msg[4].split(':')[1].strip())
            self.trips_queue.append((cname, src, dest, cnt))

        client.subscribe(self.topic)
        client.on_message = on_message


    def run(self):    
        client = self.connect_mqtt()
        client.loop_start()
        self.subscribe(client)
        time.sleep(3) #timer to look for all the trips
        client.unsubscribe(self.topic)
        client.loop_stop()
        client.disconnect()
        return self.trips_queue


class ClearTrip:

    def __init__(self):
        self.broker = 'broker.hivemq.com' 
        self.source_loc = 'IU Sample Gates' #from app
        self.destination_loc = 'Chicago Downtown' #from app
        #topic = "travel-buddy/iu-sample-gates/chicago-downtown" #from app
        self.topic = 'travel-buddy/{0}/{1}'.format(self.source_loc.lower().replace(' ','-'), self.destination_loc.lower().replace(' ','-'))
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
        
        result = client.publish(self, self.topic,'',retain = True)
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
    

    
