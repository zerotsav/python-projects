import random
import string

print(" Password Generator")

# Ask the user how long the password should be
try:
    length = int(input("Enter password length: "))
except ValueError:
    print("Please enter a valid number.")
    exit()

# Characters to use in the password
chars = string.ascii_letters + string.digits + string.punctuation

# Generate password
password = ''.join(random.choice(chars) for _ in range(length))

print("Your new password is:")
print(password)
