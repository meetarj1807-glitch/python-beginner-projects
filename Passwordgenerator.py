import secrets
import string

def generate_password(min_length, numbers = True, specialcharacter = True):
    letter = string.ascii_letters
    digits = string.digits
    special_char = string.punctuation

    characters = letter

    if numbers:
        characters += digits
    if specialcharacter:
        characters += special_char

    pwd = ""

    meets_criteria = False
    has_number = False
    has_specialchar = False

    while not meets_criteria or len(pwd) < min_length:

        new_char = secrets.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        if new_char in special_char:
            has_specialchar = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        elif specialcharacter:
            meets_criteria = meets_criteria and has_specialchar

    return pwd


min_length = int(input("Enter the No. of characters required for password : "))
has_num = input("Does number are allow (y/n) :").lower() == "y"
has_spch = input("Does special characters are allow (y/n) :").lower() == "y"
password = generate_password(8,has_num,has_spch)
print(password)

    
            