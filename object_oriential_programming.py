# #Object Orientation Programming
# x = 1
# #print(type("hello")) #gives class 'str'

# #print(type(x)) #gives class 'int'

# def hello():
#     print("hello")
# print(type(hello)) #Gives class 'function'

# str = "hello"
# print(str.upper()) #allows the string to become fully uppercase

###########


class Dog(): #allows us to define what dog is and what it can do
    def __init__(self, name, age): #allows any arguments to go through like an assignment but manually
        self.name = name #attriube called name assigned to name
        self.age = age
        # print(name)
        pass

    def get_name(self):
        return self.name #object return
    def get_age(self): 
        return self.age

    def set_age(self,age):
        self.age = age
    # def add_one(self, x):
    #     return x + 1 #method
    
    # def bark(self):
    #     print("bark") #method and operation

d = Dog("Tim", 34)
d.set_age(23)
print(d.get_age())
# d2 = Dog("Bill" , 10)
# print(d2.get_age())
# d.bark()
# print(type(d)) #gives class "__main__.dog"
# print(d.add_one(5))