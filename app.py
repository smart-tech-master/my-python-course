class Person:
    def __init__(self, name, age):
        self.name = name;
        self.age = age;

p1 = Person('Jhon', 18);
del p1.name
print(p1.name);