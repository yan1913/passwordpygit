import re

# 1. At least 2 letter between [a-z]
# 2. At least 1 number between [0-9]
# 3. At least 1 letter between [A-Z]
# 4. At least 2 character from [$!#@]
# 5. Minimum length of transaction password: 8
# 6. Maximum length of transaction password: 16
user_input = input("Please enter a password:")

def check_password_validity( user_input ) :

    
    


    
    # Condition 1
    if len( re.findall( r'[a-z]', user_input ) ) < 2 :
        return False

    if len( re.findall( r'[0-9]', user_input ) ) < 1 :
        return False

    if len( re.findall( r'[A-Z]', user_input ) ) < 1 :
        return False

    if len( re.findall( r'[$!#@]', user_input ) ) < 2 :
        return False

    if len( user_input ) < 8  :
        return False

    if len( user_input ) > 16 :
        return False

    
    return True


print(check_password_validity(user_input))
