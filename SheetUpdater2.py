import pygsheets
import os
import pandas as pd
import numpy as np
import time
from datetime import datetime

#read authentication file
keyFile=os.path.dirname(__file__)+"/Youtube Analyser-2920d371ed7e.json"

#connect to google sheet API Service
gc=pygsheets.authorize(service_file=keyFile)

sh=gc.open_by_url('https://docs.google.com/spreadsheets/d/18rLmAROIsUgQ1LcmdJLn65Gt9TLQtm8wCk5_xAPZmBk/edit?usp=sharing')

print("MOST!")
while True:
    t1=datetime.now()
    df = pd.DataFrame(np.random.randint(0,100,size=(100, 4)), columns=list('ABCD'))
    wks=sh[0]
    wks.set_dataframe(df,'A1')
    time.sleep(15)
    t2 = datetime.now()
    print(t2-t1)


