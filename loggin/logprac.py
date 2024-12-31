import logging
import os
logging.basicConfig(level=10,filename="mynewlg.txt",filemode="w",
                    format='%(asctime)s,%(name)s,%(levelname)s,%(message)s',
                    datefmt="%d/%m/%Y %I:%M:%S %p")

filename = os.path.basename(__file__)
logging = logging.getLogger(filename)
logging.critical("critical message")
logging.error("error message")
logging.warning("warning message")
logging.info("information message")
logging.debug("debug message")





