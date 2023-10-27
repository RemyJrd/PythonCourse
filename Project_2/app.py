import string
from passwdtest_app import passwdtest
from passwdgen_app import passwdgen
from passphrgen_app import passphrgen
from colorama import Fore
from PyInquirer import style_from_dict, Token, prompt

custom_style = style_from_dict({
    Token.Separator: '#6C6C6C',
    Token.QuestionMark: '#FF9D00 bold',
    Token.Selected: '#5F819D',
    Token.Pointer: '#FF9D00 bold',
    Token.Answer: '#5F819D bold',
    Token.Question: '#FF9D00 bold',
    Token.Instruction: '',
})

def main():
    while True:
        questions = [
            {
                "type": "list",
                "name": "choice",
                "message": "--- Main Menu ---",
                "choices": [
                    {"name": "--- Try a given password ---", "value": "test"},
                    {"name": "--- Generate a random password ---", "value": "generate"},
                    {"name": "--- Generate a passphrase ---", "value": "passphrase"},
                    {"name": "--- Quit ---", "value": "quit"},
                ],
            }
        ]

        answers = prompt(questions, style=custom_style)

        choice = answers["choice"]

        try:
            if choice == "test":
                password = input("Type the password to test : ")
                passwdtest(password)
            elif choice == "generate":
                lower = int(input("Amount of lowercase : "))
                upper = int(input("Amount of uppercase : "))
                numbers = int(input("Amount of digit : "))
                spec = int(input("Amount of special character : "))
                passwdgen(lower, upper, numbers, spec)
            elif choice == "passphrase":
                passphrgen()
            elif choice == "quit":
                print("----------")
                print(" --- Goodbye ! ---")
                break
            else:
                print("Invalid option")
        except InvalidOption as e:
            print(f"Erreur : {e}")

if __name__ == "__main__":
    main()

#TODO: rechecker le fonctionnement du passphrase generator
#TODO: Unit test

# Old-school CLI
""" def main_menu():
    while True:
        try:
            print("Main menu:")
            print("1. Test a given password")
            print("2. Generate a random password")
            print("3. Generate a passphrase")
            print("4. Quit")
            choice = input("Choose an option (1/2/3/4) : ")
            if choice == "1":
                password = input("Insert the password to try: ")
                passwdtest(password)
            elif choice == "2":
                lower = int(input("Number of lowercase: "))
                upper = int(input("Number of uppercase: "))
                numbers = int(input("Number of digit: "))
                spec = int(input("Number of special character: "))
                passwdgen(lower, upper, numbers, spec)
            elif choice == "3":
                passphrgen()
            elif choice == "4":
                print("----------")
                break
            else:
                print("Invalid option. Please choose between 1 and 4")
        except ValueError:
            print("Error. Please choose between 1 and 4") """
