# Initiate a class

class Employee:
    #special method/magic method/dunder method - constructor
    def __init__(self):
        print("started executing attributes/ data")
        self.Id = 2
        self.salary = 50000
        self.designation = "SDE"
        print('Attributes/Data have been executed')

    def travel(self, destination):
        print('this travel method called manually')
        print(f"YOur next travel destination is {destination}" )

# Create an object/instance of class Employee

sam = Employee()

# print(sam.salary)
sam.travel("Ladakh")
    
