import yaml
import logging

# setting the logger and specifying the path for configuration file
logging.basicConfig(level=logging.INFO)
configFilePath = './config.yaml'


# reading the configuration file
def ReadConfig():
    try:
        with open(configFilePath) as file:
            configParameters = yaml.load(file, Loader=yaml.FullLoader)
        logging.info("Configuaration file loaded successfully.")
        return configParameters
    except FileNotFoundError:
        logging.ERROR("File doesnot exist.")
