import datetime
import os
Current_datetime=datetime.datetime.now().strftime('%y-%m-%d')
extension=".txt"
filename1=Current_datetime+extension #NAME OF THE FILE
f=open(r"C:\Users\keerthana\OneDrive\Documents\filename1.txt",'w') #OPENS THE FILE
f.close()