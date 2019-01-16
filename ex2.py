class Animal():
    name = ""
    modeOfReproduction = ""
    modeOfCommunication = ""
    modeOfBreath = ""
    
    
class Mammal(Animal):
    def __init__(self):
        modeOfReproduction = "viviparously"
        modeOfCommunication = "vocalize"
        modeOfBreath = "lung breathing"
    
    def hotBlooded(self):
        print("hotBlooded")


class Insect(Animal):
    def __init__(self):
        modeOfReproduction = "oviparously"
        modeOfCommunication = "pheromonal"
        modeOfBreath = "tracheal breathing"

    def coldBlooded(self):
        print("coldBlooded")


class Dog(Mammal):
    breed = ""
    
    def __init__(self):
        modeOfReproduction = "sexual"

    def bark(self):
            print("barks")


class Bee(Insect):
    topSpeed = 0
    
    def __init__(self):
        modeOfReproduction = "asexual"

    def producesHoney(self):
        print("produces honey")

       
dog1 = Dog()
dog1.name = "Rex"
dog1.breed = "bulldog"
 


bee1 = Bee()
bee1.name = "Barry" #bee movie
bee1.topSpeed = 17

print("the name of the dog is: ", dog1.name)
print("and the breed is: ", dog1.breed)
print("the name of the bee is: ", bee1.name)
print("its top speed is:", bee1.topSpeed) 



        
        
        
