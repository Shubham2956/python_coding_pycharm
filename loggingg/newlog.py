import logging
import datetime
import os

filename = os.path.basename(__file__)
logging.basicConfig(level=10,filename="mylogeer1.txt",filemode="a",
                    format="%(name)s,%(asctime)s,%(levelname)s,%(message)s",datefmt = "%d:%m:%Y %I:%M:%S %p")

logging = logging.getLogger(filename)
print(filename)
logging.critical("critical message")
logging.info(filename)