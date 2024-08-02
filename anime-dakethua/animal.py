class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True
    def eat(self):
        print(f"{self.name} eating ")
    def sleep(self):
        print(f"{self.name} sleeping")
        
class Dog(Animal):
    def speak(self):
        print("go go go")  
class Cat(Animal):
    def speak(self):
        print("mo mo mo") 
class Mouse(Animal):
    def speak(self):
        print("fo fo fo") 

dog = Dog("cho")
cat = Cat("meo")
mouse = Mouse("chuot")

print(dog.name)
print(dog.is_alive)
dog.eat()
dog.sleep()