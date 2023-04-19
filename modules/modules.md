# <span style="font-family:Helvetica; font-size:2em;">Modules</span>

## <span style="font-family:Helvetica; font-size:1em">Working with modules</span>
To create a module just save the code you want in a file with the file extension `.py`:

Let's imagine the following situation, we have one python file named `module_first.py`. This file contains a function:
```python
def greeting(name):
    print(f"Hello, {name}")
```
And also we have another file named `module_second.py` in the same directory. 
```python
import module_first

module_first.greeting("John") # Hello, John

# Or we can use the another option
from module_first import greeting

greeting("John") # Hello, John
```
If you want to import something with a different name:
```python
from module_first import greeting as greeting_func

greeting_func("John") # Hello, John
```
You can see examples in the current directory.


