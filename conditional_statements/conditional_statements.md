# <span style="font-family:Helvetica; font-size:2em;">Conditional statements</span>

## <span style="font-family:Helvetica; font-size:1em">Working with conditional statements</span>
To define a conditional statement we must write the following code:
```python
message = "Hello world!"
if message.lower().startswith("h"):
    ...
elif message.lower().startswith("q"):
    ...
else:
    ...
```
Analog of the ternary operator:
```python
name = "John"
default_auth_message = "Hello, guest!"
auth_message = f"Hello, {name}" if name else default_auth_message 
print(auth_message)  # 'Hello, John'

```

It's important to remember that any empty data type is `False`, which means they are considered `False` in a `Boolean` context, so you can just do this:
```python
empty_dict = {}
empty_list = []
empty_string = str()

# This code says that if this variable isn't empty then
if empty_dict:
    pass

if not empty_dict:
    # This code will be executed
    pass

if not empty_list:
    # This code will be executed
    pass

if not empty_string:
    # This code will be executed
    pass
```
Also python has two built-in functions provided in python used for successive And/Or.
`Any` returns `True` if any of the items is `True`. It returns `False` if empty or all are `False`.
```python
mylist = [False, True, False]
result_for_any = any(mylist)  # True
result_for_all = all(mylist)  # False
```

You can find more information on working with conditional statements [here](https://www.w3schools.com/python/python_conditions.asp)