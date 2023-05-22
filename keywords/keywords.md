# <span style="font-family:Helvetica; font-size:2em;">Basic keywords in Python</span>
```python
def sum_func():
    return 1 + 1
```
`def` is the main keyword for defining a function.
```python
def sum_func():
    pass
```
`pass` is keyword for skipping implementation.
```python
with open("file.txt") as file:
    print(file.readlines())
```
`with` is keyword for contextmanager.

In our case, when the code from the `with` block is executed, the file will be closed. It can also be used for databases, etc.

