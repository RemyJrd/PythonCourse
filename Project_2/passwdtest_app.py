def passwdtest(passwd):

    points_per_character = 4
    points_per_lowercase = 5
    points_per_uppercase = 5
    points_per_digit = 5
    points_per_special = 6
    # !! Not ANSSI complient, fine tune the program for your use-case !!

    password_strength = 0

    for char in passwd:
        password_strength += points_per_character
        if char.islower():
            password_strength += points_per_lowercase
        elif char.isupper():
            password_strength += points_per_uppercase
        elif char.isdigit():
            password_strength += points_per_digit
        else:
            password_strength += points_per_special

    if password_strength < 64:
        print("The password is very weak.")
    elif password_strength < 80:
        print("The password is weak.")
    elif password_strength < 100:
        print("The password is moderate.")
    else:
        print("The password is strong.")

    print(f"Password Strength Score: {password_strength}")
