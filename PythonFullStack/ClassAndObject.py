class Human:
    def __init__(self, name, age, nationality, occupation):
        self.name = name
        self.age = age
        self.nationality = nationality
        self.occupation = occupation
        
        
#method
    def breathe(self):
        return f"{self.name} is breathing."
    def walk(self):
        return f"{self.name} is walking."
    def smile(self):
        return f"{self.name} is smiling."


Reshma = Human("Reshma", 21, "Indian", "Intern")
Nidhi = Human("Nidhi", 15, "Indian", "Student")

print (f"Hello I am {Reshma.name}, I am {Reshma.age}, I am {Reshma.nationality}, and i work as an {Reshma.occupation}") 
print (f"Hello I am {Nidhi.name}, I am {Nidhi.age}, I am {Nidhi.nationality},and I am a {Nidhi.occupation}")

print(Reshma.breathe())
print(Reshma.walk())
print(Reshma.smile())

print(Nidhi.breathe())
print(Nidhi.walk())
print(Nidhi.smile())
