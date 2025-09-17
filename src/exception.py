import sys     # The sys module in python provides various functions and variables that are used to manipulate         different parts of the python runtime environment
import logging
def error_msg_detail(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()         # extracts error detail and store them in exc_tb
    file_name=exc_tb.tb_frame.f_code.co_filename   # returns filename where error has occured

    error_msg = "Error occured in python script [{0}] , line number [{1}] , error message [{2}]".format(file_name,exc_tb.tb_lineno,str(error))

    return error_msg


class CustomException(Exception):            # made this class so that its easy to call the above defined function in other files
    def __init__(self,error,error_detail:sys):
        super().__init__(error)
        self.error_msg = error_msg_detail(error,error_detail=error_detail)

    def __str__(self):
        return self.error_msg
    
# below code is just for checking if the exception.py is working well
# if __name__=="__main__":
#     try:
#         a = 5
#         print(a+b)
#     except Exception as e:
#       CustomException(e, sys)
      
    