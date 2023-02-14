# classes and objects 

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)



p1 = Person("John", 36)

p1.myfunc()


# Inheritance

class Student(Person):
    def __init__(self, name, age, year):
        super().__init__(name, age)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.name, "to the class of", self.graduationyear)

x = Student("Mike", 10, 2019)
x.welcome()
x.myfunc()


# # Python also has a super() function that will make the child class inherit all the methods and properties from its parent:



