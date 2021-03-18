import math
class Calculator:
    def plus (self, x, y):
        self.first_number = x
        self.second_number = y
        return y + x
 
    def multiply (self, x, y):
        self.first_number = x
        self.second_number = y
        return y * x

    def subtract (self, x, y):
        self.first_number = x
        self.second_number = y
        return x - y
    
    def divide (self ,x, y):
        self.first_number = x
        self.second_number = y
        return x / y

nums = Calculator()
print (nums.plus(2,6))