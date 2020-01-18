#Data Manipulation
#Part 2: Password Validator
#Udirno Chaudhuri
#Checks if user's password is strong or weak

def password_strength(password):
    strong = False
    s_chars = "@*&$!"
    number = False
    length = False
    uppercase = False #counterintuitive because when both of these are false, that means at least 
    lowercase = False #----one lowercase and one uppercase
    special = False
    if len(password) >= 8:
            length = True
    for letter in password: #examines each letter in the password one by one
        strong = False
        if letter.isdigit():#for letter in password)
            number = True
        if letter.isupper(): #returns true if ALL letters are uppercase (we only want one)
            uppercase = True
        if letter.islower(): #returns true if ALL letters are lowercase (we only want one)
            lowercase = True
        if letter in s_chars:
            special = True
    if length and number and uppercase and lowercase and special:
        strong = True
        print("Strength is: strong")
        return "strong"
    else:
        strong = False
        print("Strength is: weak")
        return "weak"
        
password = input("Enter password:")
letter = password_strength(password)


