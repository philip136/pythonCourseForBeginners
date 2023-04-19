# <span style="font-family:Helvetica; font-size:2em;">Functions</span>

## <span style="font-family:Helvetica; font-size:1em">Working with functions</span>
Python has two options to define a function:
```python
def sum_func(a, b):
    return a + b

result1 = sum_func(1, 2) 
print(result1) # 3

sum_lambda_func = lambda a, b: a + b
result2 = sum_lambda_func(1, 2)
print(result2) # 3
```
Function with additional optional arguments (for sequence):
```python
def some_func(*args):
    for val in args:
        print(f"Index for {val} is {args.index(val)}")

some_func(*[1,2,3,4])
# ----------------- Result -----------------
# Index for 1 is 0
# Index for 2 is 1
# Index for 3 is 2
# Index for 4 is 3
```
Function with additional optional arguments (for dictionary):
```python
def some_func(**kwargs):
    for key, val in kwargs.items():
        print(f"Key `{key}` has value `{val}`")

some_func(**{"name": "John", "age": 26})
# or
some_func(name="John", age=26)
# ----------------- Result -----------------
# Key `name` has value `John`
# Key `age` has value `26`
```
## Decorators
When we type the characters `()` for a function, we call the magic method `__call__`  and after that function will be called:
```python
def hello_world():
    print("Hello world")

link_to_hello_world = hello_world  # <function hello_world at 0x0000021824786280>
link_to_hello_world()  # 'Hello world'
```
But we also have the opportunity to call and create a function inside another function
```python
import time
import requests

def benchmark(func):
    # Func is a link to `fetch_webpage` function
    def wrapper(*args, **kwargs):
        start = time.time()
        return_value = func(*args, **kwargs)  # The result of executing the `fetch_webpage` function
        end = time.time()
        print(f"Execution time: {end-start} seconds")
        return return_value
    return wrapper

@benchmark
def fetch_webpage(url):
    webpage = requests.get(url)
    return webpage.text

webpage_content = fetch_webpage('https://google.com')
print(webpage_content)

# ---------------- Result ----------------
# Execution time: 1.4475083351135254 seconds
# <!doctype html><html itemscope="" itemtype="http://schema.org/WebPage".......
```
