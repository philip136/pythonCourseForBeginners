# ================================ Exercise first ================================
email = "user@gmail.com".replace("gmail.com", "microsoft.com")  # 'user@microsoft.com'

# ================================ Exercise second ================================
repeated_string = "Hello" * 10  # 'HelloHelloHelloHelloHelloHelloHelloHelloHelloHello'

# ================================ Exercise third ================================
clean_string = "###Hello, World!##".strip("#")  # 'Hello, World!'

# ================================ Exercise four ================================
string_with_digits = "103\n114\n101\n101\n116\n105\n110\n103\n115"
encrypted_string = ""

for digit in string_with_digits.split("\n"):
    encrypted_string += chr(int(digit))

print(encrypted_string)  # 'greetings'
