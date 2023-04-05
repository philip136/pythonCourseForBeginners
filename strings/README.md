# <span style="font-family:Helvetica; font-size:2em;">Strings</span>

## <span style="font-family:Helvetica; font-size:1em">Working with strings</span>


To define a **STRING** we must use one of the following options:
```python
message1 = "Hello world!"  # With double quotes
message2 = 'Hello world!'  # With single quotes
```
To define a **COMMENT** we must use of the following options:
```python
# This is a single line comment that should describe the operation below 
message3 = "Hello world!"
message4 = "Hello world!"  # This is a single line comment that should describe this variable


def sum_function():
    """We usually use a multiline comment 
    when we want to describe some function or method.
    """
    pass
```
String **FORMATTING**: 
```python
name = "Bob"

greeting_msg1 = "Hello, %s" % name
greeting_msg2 = "Hello, {}".format(name)
greeting_msg3 = f"Hello, {name}"  # This method most common 
```
**SLICING** strings:
```python
# string[start:end:step]

greetings_msg = "Hello, World!"

print(greetings_msg[-1])  # '!'
print(greetings_msg[2:5])  # 'llo'
print(greetings_msg[::2])  # 'Hlo ol!'
```
String **CONCATENATION**:
```python
name = "Tom"
surname = "Smith"
full_name = name + " " + surname  # Tom Smith
```
**SEARCH SUBSTRING** in a string:
```pycon
print("Hello" in "Hello, World!")  # True
```

## <span style="font-family:Helvetica; font-size:1em">Most common methods for strings</span>
```python
greeting_msg = "Hello, World!"

# replace method 
new_greeting_msg = greeting_msg.replace("World", "John")  # 'Hello, John!'
# split method
greeting_msg_parts = greeting_msg.split(",")  # ['Hello', ' World!']
# lower method
lower_greeting_msg = greeting_msg.lower()  # 'hello, world!'
# upper method
upper_greeting_msg = greeting_msg.upper()  # 'HELLO, WORLD!'
# startswith
greeting_msg.startswith("H")  # True
# endswith
greeting_msg.endswith("!")  # True
```
Additional methods you can see [here](https://www.w3schools.com/python/python_ref_string.asp)

You can see this documentation in <code>py</code> format [here](https://github.com/philip136/pythonCourseForBeginners/blob/development/strings/string_lesson.py)

Homework after reading [here](https://github.com/philip136/pythonCourseForBeginners/blob/development/strings/HOMEWORK.md)



