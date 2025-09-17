import os
from datetime import datetime
import logging

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"   # file name {containing date and time}
logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE)  
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
     filename=LOG_FILE_PATH,
     format="[ %(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s ",   # log msg format
     level=logging.INFO,


)



# the code below is for checking working of logger.py
# import sys
# from exception import CustomException   # make sure exception.py is correct

# if __name__ == "__main__":
#     try:
#         a = 5
#         print(a + b)   # will cause NameError
#     except Exception as e:
#         logging.info("Testing logger with CustomException...")
#         custom_exc = CustomException(e, sys)
#         logging.error(custom_exc)

