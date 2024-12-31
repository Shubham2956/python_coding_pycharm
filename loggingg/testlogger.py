from loggerrr import *
import logging
import os

obj = newlog()
obj.nl()
while True:
    print("welcome to logger session")
    choice = int(input("select the choice :"))
    logging.info(f"your choice is {choice} :")
    if choice ==1:
        logging.info("nice choice")
    else:
        break


