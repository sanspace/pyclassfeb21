# class Dog:
#     """A class to model Dog behavior and info"""
#     pass

class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'

class Dog:

    kind = 'canine'         # class variable shared by all instances
    no_of_legs = 4

    def __init__(self, name, color):
        self.name = name    # instance variable unique to each instance
        self.color = color

hachi = Dog('Hachiko', 'black')
bolt = Dog('Bolt', 'white')

print(hachi.kind)
print(hachi.name)
print(hachi.color)
print(bolt.kind)
print(bolt.name)
print(bolt.color)
