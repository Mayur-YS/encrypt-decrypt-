
import datetime
import time

class random():
    @staticmethod
    def choice(list):
       now = datetime.datetime.now()
       s = int(time.strftime("%S"))
       m = int(time.strftime("%M"))
       mic = now.microsecond
       fe = mic * (m + s) % len(list)
    
       return  list[fe] 
