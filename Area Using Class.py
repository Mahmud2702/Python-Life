class shape:
    def __init__(self,a,c):
        self.a=a
        self.c=c 
        #area = (0.5*self.a*self.b)
        #print("Area = ",area)
    def area(self):
        print("Nothing") 


class triangle(shape):
    def area(self):
        area = .5*self.a*self.c
        print("Area1= ",area) 


class rectangle(shape):
    def area(self):
        area = (self.a*self.c)  
        print("Area2= ",area)

s1= shape(10,20)
s1.area()
s= triangle(5,10)
s.area()
t= rectangle(10,20)
t.area()