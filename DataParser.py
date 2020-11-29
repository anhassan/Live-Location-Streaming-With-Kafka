import json
import datetime
import logging, uuid

# setting the logger and specifying the basic configuration
logging.basicConfig(level=logging.INFO)


# reading the input JSON file
def getJsonData(filePath):
    try:
        with open(filePath) as jsonFile:
            jsonRouteData = json.load(jsonFile)
        logging.info("JSON input loaded successfully.")
        return jsonRouteData
    except FileNotFoundError:
        logging.ERROR("File doesnot exist.")


# parsing the Json input and extracting the latitude and longitude information
def jsonToCoordinates(jsonRoute):
    jsonCoordinatesList = [[x, y] for jsonFeatures in jsonRoute['features']
                           for x, y in jsonFeatures['geometry']['coordinates']]
    return jsonCoordinatesList


# creating Json output object for Kafka producer
def getJsonObject(coordinates, bus_id):
    routeObjectList = [{"key": bus_id + "-" + str(uuid.uuid4()), "timestamp": str(datetime.datetime.utcnow()),
                        "longitude": x, "latitude": y} for x, y in coordinates]
    return routeObjectList
