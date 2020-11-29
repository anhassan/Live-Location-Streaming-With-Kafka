import numpy as np
import pandas as pd
from multiprocessing import Process
from KafkaJsonProducer import KafkaJsonProducer
import ConfigurationReader as configReader


def runProducersInParallel(*functions):
    processList = []
    for function in functions:
        process = Process(target=function)
        process.start()
        processList.append(process)
    for process in processList:
        process.join()


# accessing the constants from the configuration file
configParameters = configReader.ReadConfig()
TOPIC_NAME = configParameters["topic_name"]
HOST_ADDRESS = configParameters["host_ip"]
FILE_PATHS = configParameters["file_paths"]

# List of Id's for buses
busIds = ["0001", "0002", "0003"]

# Instanciating three Kafka producers for three buses
kafkaBusProducer1 = KafkaJsonProducer(busIds[0], TOPIC_NAME, HOST_ADDRESS, FILE_PATHS,loop=1)
kafkaBusProducer2 = KafkaJsonProducer(busIds[1], TOPIC_NAME, HOST_ADDRESS, FILE_PATHS,loop=1)
kafkaBusProducer3 = KafkaJsonProducer(busIds[2], TOPIC_NAME, HOST_ADDRESS, FILE_PATHS,loop=1)

# Sending data concurrently through multiprocessing
if __name__ == '__main__':
    runProducersInParallel(kafkaBusProducer1.sendLocationData, kafkaBusProducer2.sendLocationData
                           , kafkaBusProducer3.sendLocationData)

