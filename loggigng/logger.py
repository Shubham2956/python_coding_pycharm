import logging

logging.basicConfig(level=10,filename="mylog.txt",format='%(asctime)s:%(name)s:%(levelname)s:%(message)s',
                    datefmt="%d/%m/%Y %I:%M:%S %p")
logger = logging.getLogger("logger1")

logger.critical("critical message")
logger.error("error message")
logger.warning("warning message")
logger.info("information message")
logger.debug("debug message")


while True:
    print("1.covid check \n2.maleria check \n3.cancer check")
    choice = int(input("enter the choice"))
    logging.info(f"choice processed {choice}")
    if choice ==1:
        logging.info("covid status checking.......")
    elif choice==2:
        logging.info("maleria status checking.........")
    elif choice==3:
        logging.info("cancer status checking..............")

    else:
        logging.info("invalid input . ")
        try:
            ch =int(input("do you want to continue : y|n"))
            if ch =="no":
                logging.info("thank you")

                break

        except ValueError as msg:
            logging.exception(msg)