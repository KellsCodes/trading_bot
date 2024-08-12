import logging as lg
import os
from datetime import datetime


def initialize_logger():

    # Creating a log folder for the logs
    logs_path = './logs/'
    try:
        os.mkdir(logs_path)
    except OSError:
        print(
            "Creation of the directory %s failed - it does not have to be bad" % logs_path)
    else:
        print("Successfully created log directory.")

    # Renaming each log on the time
    log_name = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
    log_name += ".log"

    # Writing logs to log dir
    lg.basicConfig(
        level=lg.DEBUG,
        format='%(asctime)s - %(levelname)s: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        filename=f"{logs_path}/{log_name}",
    )
    # Log to stdout
    lg.getLogger().addHandler(lg.StreamHandler())

    # init message
    lg.info('Log initialized.')

