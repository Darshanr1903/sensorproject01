import logging
import os
from datetime import datetime
LOG_FILE_PATH=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%s')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s]%(lineno)d%(name)s-%(levelename)s-%(message)s",
    level=logging.INFO()
)