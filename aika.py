import time
from datetime import date
from datetime import datetime
def aika():
    #Date today
    today = date.today()

    datetime_month = today.month
    datetime_day = today.day
    #Combining date ja month
    aika_tänään = (f'{datetime_day}.{datetime_month}')
    #Convert to string format
    inputText = aika_tänään
    return inputText
