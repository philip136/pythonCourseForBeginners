# <span style="font-family:Helvetica; font-size:2em;">Homework</span>
This homework assignment contains three exercises of varying difficulty levels.
> Exercises
1. Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area. 
2. Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.
3.Define a class that has a method that will return all instance attributes.
```python
class A:
    def __init__(self, **kwargs):
        for key, val in kwargs.items():
            setattr(self, key, val)
    
    def attributes(self):
        ...
```
3. Define a class via `type` keyword.

**Good luck to you** :wink: