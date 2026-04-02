class Shape:
    def __init__(self,h=0,w=0,r=0):
        self.h = h
        self.w = w
        self.r = r

class Rect(Shape):
    def __init__(self,h,w):
        super().__init__(h=h,w=w)

    def area(self):
        print(f'area of rect is {self.h*self.w}')    

class Circle(Shape):
    def __init__(self,r):
        super().__init__(r=r)

    def area(self):
        print(f'area of circle is {3.14 * (self.r ** 2)}')           

r = Rect(5,6)        
c = Circle(4)

for x in(r,c): 
    x.area()