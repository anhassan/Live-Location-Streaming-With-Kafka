import ConfigurationReader as configReader
import DataParser as parser
from pykafka import KafkaClient
import json, logging

# setting the logger and specifying the basic configuration
logging.basicConfig(level=logging.INFO)


class KafkaJsonProducer:
    def __init__(self, bus_id, topic_name, host_ip, file_paths,loop):
        logging.info("Created Kafka Producer.")
        self.bus_id = bus_id
        self.topic_name = topic_name
        self.host_ip = host_ip
        self.file_path = file_paths[int(bus_id[-1]) - 1]
        self.loop = loop

    def generateJsonObject(self):
        # fetch and parse the input location data
        jsonInput = parser.getJsonData(self.file_path)
        jsonCoordinates = parser.jsonToCoordinates(jsonInput)

        # make json output for the Kafka producer to send
        jsonLocationObject = parser.getJsonObject(jsonCoordinates, self.bus_id)
        return jsonLocationObject

    def sendData(self,message,kafkaProducer,loop):
        iterator = 0
        threshold = len(message)-1
        while(iterator<threshold):
            kafkaProducer.produce(json.dumps(message[iterator]).encode("utf-8"))
            iterator+=1
            if(iterator==threshold) and loop : iterator=0


    def sendLocationData(self):
        logging.info("Sending data to Kafka consumer for BUS_ID : " + self.bus_id)
        clientKafka = KafkaClient(hosts=self.host_ip)
        topicKafka = clientKafka.topics[self.topic_name]
        producerKafka = topicKafka.get_sync_producer()
        messageToSend = self.generateJsonObject()
        self.sendData(messageToSend,producerKafka,self.loop)

