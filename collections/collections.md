# <span style="font-family:Helvetica; font-size:2em;">Collections</span>

## <span style="font-family:Helvetica; font-size:1em">Working with collections</span>
> Python has four collection data types:
1. `List`
2. `Tuple`
3. `Set`
4. `Dictionary`
# List (Mutable)
```python
fruit_list = ["apple", "banana", "cherry"]

# Indexing operation
print(fruit_list[0]) # apple
print(fruit_list[-1])  # cherry

# Add operation
fruit_list.append("pear")
print(fruit_list)  # ["apple", "banana", "cherry", "pear"]

# Reverse list
print(fruit_list[::-1])  # ['pear', 'cherry', 'banana', 'apple']

# Replace object
fruit_list[0] = "watermelon"
print(fruit_list)  # ["watermelon", "banana", "cherry", "pear"]
```
Additional methods for working with lists you can see [here](https://www.w3schools.com/python/python_ref_list.asp)

# Set (Mutable)
The set doesn't have duplicate records.
```python
fruit_set = {"apple", "banana", "cherry"}
fruit_set.add("apple")
print(fruit_set)  # {"apple", "banana", "cherry"}
```
Additional methods for working with sets you can see [here](https://www.w3schools.com/python/python_ref_set.asp)


# Dictionary (Mutable)
```python
personal_data = {"name": "John", "age": 23}
print(personal_data["name"]) # 'John'
print(personal_data.get("name")) # 'John'

print(personal_data["surname"]) # KeyError: 'surname'
print(personal_data.get("surname"))  # None, we have opportunity to pass a second argument to get method will default to None
```
Additional methods for working with dictionaries you can see [here](https://www.w3schools.com/python/python_ref_dictionary.asp)

# Tuple (Immutable)
Same as this list, but without the ability to change or add value
```python
fruit_tuple = ("apple", "banana", "cherry")
fruit_tuple[0] = "watermelon"  # TypeError: 'tuple' object does not support item assignment
```
Additional methods for working with tuples you can see [here](https://www.w3schools.com/python/python_ref_tuple.asp)

Homework after reading [here](https://github.com/philip136/pythonCourseForBeginners/blob/development/collections/homework.md)
