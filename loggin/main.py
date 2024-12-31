import logging
import os

class orbit:
    def orlog(self):
        filename = os.path.basename(__file__)

        logger = logging.getLogger(filename)
        logging.basicConfig(level=10, filename="detail.txt", format='%(asctime)s:%(name)s:%(levelname)s:%(message)s',
                            datefmt='%d/%m/%Y  %I:%M:%S %p')



class one():
    def new(self):
        while True:
            print("1.age_check\n2.covid_check\n3.vaccine_status")
            choice = int(input("enter the valid choice:"))
            logging.info(f"your choice is {choice}")

            if choice == 1:
                print("age is confirmed")
                logging.info("age_checked verified")
                ch =input("do you want to continue:   [yes/no] ")
                if ch == "no":
                    print("thank you for using")
                    logging.info("thank you")
                    break


            elif choice == 2:
                print("covid status checked")
                logging.info("covid_status confirmed")
                ch = input("do you want to continue:   [yes/no] ")
                if ch == "no":
                    print("thank you for using")
                    logging.info("thank you")
                    break


            elif choice == 3:
                print("vaccine status is checked")
                logging.info("vaccine status complete")
                ch =input("do you want to continue:   [yes/no] ")
                if ch == "no":
                    print("thank you for using")
                    logging.info("thank you")
                    break


            else:
                print("please give correct choice")
                logging.error("please give correct response")
                try:
                    ch =input("do you want to continue:   [yes/no] ")
                    if ch == "no":
                        print("thank you for using")
                        logging.info("thank you")
                        break

                except ValueError as msg:
                    logging.error(msg)


obj1 = orbit()
obj1.orlog()
obj=one()
obj.new()







