import math
class Rectangel:
    def __init__ (self, x, y):
        self.lenght = x
        self.width = y

    def area(self):
        return (self.lenght * self.width)
    
    def perimeter(self):
        return (self.lenght + self.width) * 2

    def print_info(self):
        print('P =',nums.perimeter(),"\t","S =",nums.area(),
        "\t","lenght =",self.lenght,"\t","Width =",self.width)
nums = Rectangel(15,40)
nums.print_info()


