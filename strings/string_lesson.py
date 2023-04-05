message1 = "Hello world!"  # With double quotes
message2 = 'Hello world!'  # With single quotes

# This is a single line comment that should describe the operation below
message3 = "Hello world!"
message4 = "Hello world!"  # This is a single line comment that should describe this variable


def sum_function():
    """We usually use a multiline comment
    when we want to describe some function or method.
    """
    pass


name = "Bob"

greeting_msg1 = "Hello, %s" % name
greeting_msg2 = "Hello, {}".format(name)
greeting_msg3 = f"Hello, {name}"  # This method most common

greetings_msg = "Hello, World!"

print(greetings_msg[-1])  # '!'
print(greetings_msg[2:5])  # 'llo'
print(greetings_msg[::2])  # 'Hlo ol!'

name = "Tom"
surname = "Smith"
full_name = name + " " + surname  # Tom Smith

print("Hello" in "Hello, World!")  # True

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
