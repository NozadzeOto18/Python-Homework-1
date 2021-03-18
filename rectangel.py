import math
class Rectangel:
    def __init__ (self, lenght, width):
        self.lenght = lenght
        self.width = width
        
    def area(self):
        return (self.lenght * self.width)
    
    def perimeter(self):
        return (self.lenght + self.width) * 2

    def print_info(self):
        print(f"area - {nums.area()},  perimeter - {nums.perimeter()},  width - {self.width},  lenght - {self.lenght}")
nums = Rectangel(15,40)
nums.print_info()


