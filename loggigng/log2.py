import logging

logging.basicConfig(level=10 , filename='mylog1.txt',filemode='a', format= '%(asctime)s:%(name)s:%(levelname)s:%(message)s',datefmt="%d/%m/%Y %I:%M:%S %p")
logger = logging.getLogger("log2")

logger.critical("critical issue")
logger.error("error issue")
logger.warning("warning issue")
logger.info("information issue")
logger.debug("debug issue")



