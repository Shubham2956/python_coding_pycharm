import logging
import os
class newlog:
    filename = os.path.basename(__file__)
    logger = logging.getLogger(filename)
    def nl(self):
        logging.basicConfig(level=10,filename="mynewloger.txt",filemode="a",
                        format="%(asctime)s:%(name)s:%(levelname)s %(message)s",datefmt="%d/%m/%Y %I:%M:%s %p")
