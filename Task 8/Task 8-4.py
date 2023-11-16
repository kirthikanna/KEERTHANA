#4)KINDLY VISIT THE BELOW LINK AND CONVERT THE URL DIAGRAM INTO CLASS AND METHODS
#https://github.com/rvsp/typescript-oops/blob/master/Practice/TV-class.md
class tv:#PARENT CLASS OR BASE CLASS
    def __init__(sony,price,inches,OnOffstatus,volume,channel,v=50,c=1):
        sony.price=price
        sony.inches=inches
        sony.OnOffstatus=OnOffstatus
        sony.volume=volume
        sony.channel=channel
        sony.v=v
        sony.c=c
    def decreasevolume(sony):#THE METHOD TO DECREASE THE VOLUME OF TV
        if sony.volume>=100:
            sony.volume=sony.volume-10
            print("decreased the tv volume")
    def increasevolume(sony):#THE METHOD TO INCREASE THE VOLUME OF THE TV
        if sony.volume>=0 & sony.volume<=100:
            sony.volume=sony.volume+10
            print("increased the tv volume to",sony.volume)
    def cha(sony):#TO DISPLAY THE CHANNEL NUMBER OF THE TV
        if sony.channel<=50:
            print("channel number is",sony.channel)
        else:
            print("you have entered the invalid channel number")
    def resetTv(sony):#METHOD TO RESET THE TV
        print("tv reseted to default volume and channel")
        print("the default volume of tv is",sony.v)
        print("the default channel of tv is",sony.c)
    def status(sony):#METHOD TO DISPLAY THE STATUS OF THE TV
        print("the sony tv is at channel number", sony.channel , "and volume of tv is",sony.volume)
class Led(tv):#SUBCLASS AND WE USED THE CONCEPT OF INHERITANCE
    def __init__(sony,price,inches,ONOffstatus,volume,channel,screenthickness,energyusage,lifespan,refreshrate,viewingangle,backlight):
        super().__init__(price,inches,ONOffstatus,volume,channel)
        sony.screenthickness=screenthickness
        sony.energyusage=energyusage
        sony.lifespan=lifespan
        sony.refreshrate=refreshrate
        sony.viewingangle=viewingangle
        sony.backlight=backlight
        
    def display(sony):#THE METHOD TO DISPLAY THE ADDITIONAL FEATURES OF THE TV
        print("the additional features of tv are")
        print("screen thickness is",sony.screenthickness)
        print("energy usage of tv is ",sony.energyusage)
        print("life span of tv is",sony.lifespan)
        print("refreshrate of tv is",sony.refreshrate)
        print("viewing angle of tv is",sony.viewingangle)
        print("backlight of tv is",sony.backlight)
class plasma(Led):#SUBCLASS AND WE USED THE CONCEPT OF INHERITANCE
    pass   
t=plasma(50000,55,'onoff',10,30,1,'20kw','20years','0.5sec','31degress','75percent')  
t.increasevolume()#CALLING THE METHOD OF A CLASS
t.decreasevolume()
t.cha()
t.resetTv()
t.status()
t.display()
