# <span style="font-family:Helvetica; font-size:2em;">Exceptions</span>

## <span style="font-family:Helvetica; font-size:1em">Working with exceptions</span>
Implemented as in most languages, only the keyword `catch` is replaced by `except`
```python
try:
    result = 1 / 0
except ZeroDivisionError as exception:
    print(str(exception))
# -------------- Result --------------
# division by zero
```
In Python, all exceptions must be instances of a class that derives from BaseException. If you would like to create a new exception, you should use the following implementation:
```python
class MyException(BaseException):
    def __str__(self):
        return "It's my exception"

raise MyException() # __main__.MyException: It's my exception
```
The keyword `raise` is the same as `throw` in Java for example.
