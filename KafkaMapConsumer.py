import time
from flask import Flask,Response,render_template
from pykafka import KafkaClient
import ConfigurationReader as configReader
from kafka import KafkaConsumer


# accessing the constants from the configuration file
configParameters = configReader.ReadConfig()
TOPIC_NAME = configParameters["topic_name"]
HOST_ADDRESS = configParameters["host_ip"]
FILE_PATHS = configParameters["file_paths"]

# Instanciating a Kafka Consumer listening to the desired topic
def getKafkaConsumer(topicName):
    consumerKafka = KafkaConsumer(topicName,
                         bootstrap_servers=[HOST_ADDRESS],
                         group_id=None,
                         auto_offset_reset='smallest')
    return consumerKafka

# Forming a stream of message sent through the Kafka producers
def getStreamMessages(consumerKafka):
    for message in consumerKafka:
        time.sleep(0.25)
        if message is not None:
            yield 'data:{0}\n\n'.format(message.value.decode())



# Instanciating the Flask Application
app = Flask(__name__)

# Forming the homepage endpoint
@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/topic')
def routeTopic():
    return Response(getStreamMessages(getKafkaConsumer(TOPIC_NAME)), mimetype="text/event-stream")


if __name__ == '__main__':
    app.run(debug=True,port=5001,threaded=True)



