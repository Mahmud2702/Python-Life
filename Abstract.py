from abc import ABC, abstractmethod
class shape:
    def __init__(self,a,c):
        self.a=a
        self.c=c 
    @abstractmethod   
    def area(self):
        pass


class triangle(shape):
    def area(self):
        area = .5*self.a*self.c
        print("Area1 =",area) 


class rectangle(shape):
    def area(self):
        area = (self.a*self.c)  
        print("Area2 =",area)

s= triangle(5,10)
s.area()
t= rectangle(10,20)
t.area()