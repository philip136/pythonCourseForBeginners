# <span style="font-family:Helvetica; font-size:2em;">Classes</span>

## <span style="font-family:Helvetica; font-size:1em">Working with classes</span>
To create a class, use the keyword `class`, each method of class has a required argument `self` (analogue of `this`).
The keyword `self` is a link to an instance of class.
```python
class Human:
    def __init__(self, name, weight, height):
        self.name = name
        self.weight = weight
        self.height = height
    
    def run(self):
        print(f"Human with name {self.name} is running")

human = Human(name="John", weight=80, height=180)
human.run() # Human with name John is running
print(human) # <__main__.Human object at 0x000002182474EF70>

```
## Basic inheritance
```python
class Person:
  def __init__(self, first_name, last_name):
    self.first_name = first_name
    self.last_name = last_name

class Student(Person):
    pass
```
## Multiple Inheritance
```python
# Find a good example
```

All methods that start and end with a double underscore `__` have a specific name `magic methods`.
In the example above, the magic method is the method `__init__` it's a constructor.
The most useful magic methods:
```python
class Person:
    def __init__(self, name, height):
        self.name = name
        self.height = height
    
    def __str__(self):
        return f"Person {self.name}"
    
    def __repr__(self):
        return f"Person object {self.name}"
    
    def __eq__(self, other):
        return self.name == other.name

    
person1 = Person("John", 180)  # Person object John (because we overriden __repr__ method)
person2 = Person("John", 193)  # Person object John (because we overriden __repr__ method)
print(person1) # Person John (because we overriden __str__ method)
print(person1 == person2) # True, because we compare by name (we overriden __eq__ method)
```