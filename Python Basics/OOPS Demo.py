# Classes are nothing but blueprint or prototype.
# Class can have class variable, instance variable, constructor etc.
# Objects are created for a class

class Calculator:
    num = 100

    def getData(self):
        print('I am now executing as a method in the class')

obj = Calculator() # syntax to create objects in python
obj.getData()
print(obj.num)