# password strength checker
# objective:
# the objective of this project is to build a password strength checker that 
# evaluates the strength of uer-provided password based on common security criteria.
# the programe helps uers create secure password by providing feedlback on password quality and suggesting improvements.

# topic covered in  python 
# functions, conditonal statements, loops,input and output handling , sting maipulation.
# import library (regular expressions), logic validation etc

import re # regular expression module.
# min 8 chars, digit, upper case, lower case & special charactristics

def check_password_strength(password):
    if len(password) < 8: # length of password
        return "weak: password must be at least 8 charatristics."
    
    if not any (char.isdigit() for char in password):
        return "weak: password must be contain a digit."
    
    if not any (char.isupper() for char in password):
        return "weak: password must be contain an upper letter."
    
    if not any (char.islower() for char in password):
        return "weak: password must be contain an lower letter." 
    
    if not re.search(r'[!@#$%^&*(){}.?]', password):
        return "medium: password must contain a special char"
    
    return "strng: your password is secured !"

def password_checker():
    print("welcome to the password strength checker.")

    while True:
        password = input("Enter your password (or type'exit' to quit):")

        if password.lower() == 'exit':
            print("thank you for usig this tool")
            break

        result = check_password_strength(password)
        print(result)


# run the password checker tool
if __name__ == "__main__":
    password_checker()

