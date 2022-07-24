import logging


class LogGen:
    @staticmethod
    def loggen(self):
        logging.basicConfig(filename="./Logs/Automation.log",
                            format='[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s',
                            datefmt='%H:%M:%S'
                            )
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger

# Missed requiremnet file
# Readme file missing
# Reports/ Json/ HTML/Screenshots
# Src pytest/ env/ requirement same
