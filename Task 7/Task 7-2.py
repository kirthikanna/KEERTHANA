import datetime
import os
f = open("filename1.txt",'w') #UPDATING THE EXISTING FILE 
#f.write( datetime.datetime.now().strftime('%y-%m-%d'))
 #WRITING THE CONTENT IN THE TEXT FILE
f.write("the content in that file 23-10-2023")
f.close()   #CLOSING THE FILE.