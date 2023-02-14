class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f'name: {self.name} \n age: {self.age}'

def main():
    p1 = Person("mike", 36)
    p2 = Person("john", 34)
    print(p1)
    print(p2)
main()