import module_first

module_first.greeting("John")  # Hello, John

from module_first import greeting

greeting("John")  # Hello, John

from module_first import greeting as greeting_func

greeting_func("John")  # Hello, John
