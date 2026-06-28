"""
Password generator by BRUHmeh

You can modify whatever you want and change it own code
"""

import os
import string
import random
import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)

# ------------------------------

s = string

letters_tiny = s.ascii_lowercase
letters_big = s.ascii_uppercase
symbles = s.punctuation
numbers = s.digits
spaces = s.whitespace

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def password_generator(length):
    return ''.join(random.choice(letters_tiny + letters_big + symbles + numbers) for each in range(length))
#                                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^  change this to whatever you want

clear_screen()

while True:
    try:
        clear_screen()
        pass_length = int(input("Enter the length of the password/s: "))
        num_passwords = int(input("Enter the number of password/s to generate: "))
        clear_screen()
        break

    except ValueError as e:
        clear_screen()
        print(f"ERROR: {e}", '\n')



while True:
    input('Press enter to generate... ')
    clear_screen()
    for num in range(num_passwords):
        print(Fore.RED + password_generator(length=pass_length))
    print()