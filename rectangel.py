import math
class Rectangel:
    def __init__ (self, x, y):
        self.lenght = x
        self.width = y

    def area(self, x, y):
        self.x = x
        self.y = y
        return (x * y)
    
    def perimeter(self, x, y):
        self.x = x
        self.y = y
        return (x + y) * 2

    def print_info(self, x, y):
        self.x = x
        self.y = y
        print('P =',nums.perimeter(x ,y),"\t","S =",nums.area(x, y),"\t","lenght =",x,"\t","Width =",y)
nums = Rectangel(3,4)
nums.print_info(nums.lenght , nums.width)


