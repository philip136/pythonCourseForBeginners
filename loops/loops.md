# <span style="font-family:Helvetica; font-size:2em;">Loops</span>

## <span style="font-family:Helvetica; font-size:1em">Working with loops</span>

Python has two kind of loops: `while` and `for`.
The `for` loop is defined as follows:
```python
fruits = ["apple", "banana", "pear"]

for fruit in fruits:
    pass
```
The `while` loop is defined as follows:
```python
i = 1

while i < 5:
    print(i)
    i += 1
```
If we have a task to get certain values from a list, we have two possibilities to do this.
Let's imagine the following situation when we have a list of names, and we want to get all the names that start with the letter 'A'
```python
names = ["Amelia", "Bob", "Adam", "John", "Alexander"]

# First solution 
certain_names = []

for name in names:
    if name.startswith("A"):
        certain_names.append(name)
        

# Second solution via list comprehension
certain_names = [name for name in names if name.startswith("A")]
```

> You can find more information about working with loops:
1. `for` loop [here](https://www.w3schools.com/python/python_for_loops.asp)
2. `while` loop [here](https://www.w3schools.com/python/python_while_loops.asp)

Homework after reading [here](https://github.com/philip136/pythonCourseForBeginners/blob/development/loops/homework.md)
