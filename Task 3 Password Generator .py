import random
import string

def generate_password(length, use_letters, use_numbers, use_symbols):
    chars = ""

    if use_letters:
        chars += string.ascii_letters

    if use_numbers:
        chars += string.digits

    if use_symbols:
        chars += string.punctuation

    if not chars:
        return None

    password = ""

    for _ in range(length):
        password += random.choice(chars)

    return password

print("Password Generator")

length = int(input("Enter password length: "))

letters = input("Include Letters? (yes/no): ").lower() == "yes"
numbers = input("Include Numbers? (yes/no): ").lower() == "yes"
symbols = input("Include Symbols? (yes/no): ").lower() == "yes"

password = generate_password(length, letters, numbers, symbols)

if password:
    print("\nGenerated Password:", password)
else:
    print("Please select at least one character type.")