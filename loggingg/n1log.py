import logging


logging.basicConfig(level=10,format="%(asctime)s :%(name)s :%(levelname)s:%(message)s", filemode="a" ,filename="alog.txt",
                    datefmt="%d/%m/%Y %I:%M:%S %p")