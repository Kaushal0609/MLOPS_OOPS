# Base class
# class Animal:
#     def __init__(self,name):
#         self.name = name

#     def speak(self):
#         print(f"{self.name} makes a sound")

# # Derived class
# class Dog(Animal):
#     def speak(self):
#         print(f"{self.name} barks")

# animal = Animal("Generice ANimal")
# animal.speak()

# dog = Dog("Leo")
# dog.speak()


# SUPER KEYWORD

class Animal:
    def __init__(self):
        self.name = "Generic animals"
    
    def speak(self):
        print(f"{self.name} makes a sound")

# Derived class

class Dog(Animal):
    def __init__(self, breed):
        super().__init__()
        self.breed = breed

    def speak(self):
        super().speak()
        print(f"{self.name} barks and it is a {self.breed}")

dog = Dog("leo")
dog.speak()