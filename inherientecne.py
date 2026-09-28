class Pet: #Example of the ALPHA AWOOO Class
     def __init__ (self, name, age):
          self.name = name
          self.age = age
     def show(self):
          print(f"I am {self.name} and I am {self.age}")
          print("I dont know what noise I make.")
        
class Cat(Pet): #Child class also having pet inherience what class Pet is

    def speak(self):
        print("Meow")

class Dog(Pet): #Child Class
    def __init__ (self, name, age, color):
          super().__init__(name,age) #inherience the super class to make my life easier to read
          self.color = color
    def show(self):
              print(f"I am {self.name} and I am {self.age}. I am also {self.color}")
    def speak(self):
        print("BARK")

p = Pet("timothy", 14)
p.show()
input()
c = Cat("Billy", 7)
c.show()
c.speak()
input()
d = Dog("Jillin", 3, "white")
d.show()
d.speak()