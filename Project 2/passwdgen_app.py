import random
import string
import math
from passwdtest_app import passwdtest

def passwdgen(lowerc, upperc, numb, spec):
    characters = ""

    if lowerc > 0:
        characters += string.ascii_lowercase
    if upperc > 0:
        characters += string.ascii_uppercase
    if numb > 0:
        characters += string.digits
    if spec > 0:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(lowerc + upperc + numb + spec))
    entropy = calculate_entropy(password)
    passwdtest(password)
    print(f"Password Generated : {password}")
    print(f"entropy : {entropy:.1f}")
    input("To go to main menu, press enter: ")

def calculate_entropy(password):
    char_set = set(password)
    char_set_size = len(char_set)
    password_size = len(password)
    entropy = math.log2(char_set_size ** password_size)
    return entropy
