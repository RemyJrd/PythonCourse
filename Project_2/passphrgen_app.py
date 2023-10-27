import random

def passphrgen():
    with open(r'C:\Users\remyj\pythonc\Project_2\eff.txt', 'r') as file:
        lines = file.readlines()

    word_dict = {}
    for line in lines:
        parts = line.split('\t')
    if len(parts) == 2:
        key, value = parts
        key = key.strip()
        value = value.strip()
        if key in word_dict:
            word_dict[key].append(value)
        else:
            word_dict[key] = [value]
    password = []
    for _ in range(6):
        random_number = ''
    for _ in range(5):
        random_number = random_number + str(random.randint(1, 6))
        words = word_dict.get(random_number, ['unknown'])
        chosen_word = random.choice(words)
        password.append(chosen_word)

    print("Generated password :")
    print(" ".join(password))
    input("To go to main menu, press enter: ")
