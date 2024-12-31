import logging
import os
filename = os.path.basename(__file__)
logging.basicConfig(level=10,format="%(asctime)s:%(name)s:%(levelname)s:%(message)s",filename="myloggi.txt"
                    ,datefmt="%d/%m/Y %I:%M:%S %p",)


logging = logging.getLogger(filename)
while True:
    print("1.checking age\n 2.checing covid status\n 3.checking vaccination status")
    choice = int(input("enter the your choice :"))
    print(f"your choice is {choice}.")
    if choice == 1:
        logging.info("age status checking....")
    elif choice == 2:
        logging.info("covid status checking....")
    elif choice == 3:
        logging.info("vaccination status checking....")
    else:
        logging.error("please enter correct choice")
        try:
            ch = int(input("do you want to continue [y/n].....:"))
            if ch == "no":
                logging.info("application closed...")
                break
        except ValueError as msg:
            logging.exception(msg)
