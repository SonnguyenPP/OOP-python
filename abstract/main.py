from abc import ABC, abstractmethod

class Vehicle(ABC):
 
    def go(self):
        pass
    
 
    def stop(self):
        pass
    
class Car(Vehicle):
    
    def go(self):
        print("you drive the car")
        
    def stop(self):
        print("you stop the car")
        
class Moto(Vehicle):
    
     def go(self):
       print("you drive the Moto")
    
     def stop(self):
        print("you stop the Moto")
    
moto = Moto()

moto.go()
moto.stop()