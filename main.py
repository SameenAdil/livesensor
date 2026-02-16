from sensor.exception import SensorException
import sys
import os
from sensor.logger import logging


def test_exception():
    try:
        logging.info("here, a error occur!")
        a= 1/0
    except Exception as e:
        raise SensorException(e,sys)
        #raise e

if __name__ == "__main__":  #prevent execution on import
    try:
        test_exception()
    except Exception as e:
        print(e)