class A:
    def display1(self):
        print("I am in A class")

class B(A):
    def display2(self):
        print("I am in B class")

class C(B):
    def display3(self):
        print("I am in C class")

obj = C()
obj.display1()
obj.display2()
obj.display3()
