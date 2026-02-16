import sys
import os


def error_message_detail(error,error_detail:sys):
    #error_detail is a module of sys library and exc_info()
    #give 3 things in tuple, first 2 not required
    _,_,exc_tb = error_detail.exc_info() 
    filename = exc_tb.tb_frame.f_code.co_filename

    error_message = f"""Error occured, the filename is {filename},
    the line number is {exc_tb.tb_lineno} and the 
    error is {error}"""

    return error_message


class SensorException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
   #error_detail mean how to capture line number, file name in which error occur, and what is the error

        self.store_error_msg = error_message_detail(error_message,
                            error_detail=error_detail)
     
    def __str__(self):
        return self.store_error_msg