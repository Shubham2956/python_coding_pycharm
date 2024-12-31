import logging
import os
filename = os.path.basename(__file__)
logging.basicConfig(level=10,filename="myloggi.txt",filemode='a',
                    format='%(asctime)s ,%(name)s :%(levelname)s:%(message)s',datefmt='%d/%m/%Y  %I/%M/%S')


logging = logging.getLogger(filename)
logging.critical("critical message")
logging.error("error message")
logging.warning("warning message")
logging.info("info message")
logging.debug("debug message")
