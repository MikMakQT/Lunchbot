import time
from datetime import date
from datetime import datetime
def aika():
    #DATE, but it has year inside it
    today = date.today()
    #Need to split day and month from today
    datetime_month = today.month
    datetime_day = today.day
    #day + month
    day_today = (f'{datetime_day}.{datetime_month}')
    #Convert to string type
    
    return day_today
