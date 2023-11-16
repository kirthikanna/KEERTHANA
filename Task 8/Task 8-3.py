class list1:
    def __init__(self,l):
        self.l=l
        self.pi=3.141
    def area(self):
        print("the area of circle of the given list is")
        for i in range(8):
            print(self.pi*self.l[i]*self.l[i])
    def perimeter(self):
        print("the perimeter of circle of the given list is")
        for i in range(8):           
            print(2*self.pi*self.l[i])
c=list1(l=[10,501,22,37,100,999,87,351])
print(c.area())
print(c.perimeter())