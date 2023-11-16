#2)CREATE A PRIVATE CLASS VARAIBLE AND USE IT IN THE TASKLIKE PI=3.141
class aop:
    def __init__(self,r):
        self.r=r
    def area(self):
        self.__pi=3.141 #creating a private variable in class
        return self.__pi*self.r*self.r
a=aop(5)
print("area of a circle by using private variable in class  is",a.area())