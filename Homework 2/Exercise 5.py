def main():
    
    inputPassword = input("Enter: ")
    if valid_password(inputPassword) == True:
        print('Valid')
    else:
        print('Invalid')
    print(valid_password(inputPassword))

def valid_password(inputPassword):
    characters = True
    alpha = True
    pancakes = False
    
    if len(inputPassword) < 10:
        characters = False
    if inputPassword.isalnum() != True:
        alpha = False
        
    upper = False
    lower = False
    digit = False
    for i in inputPassword:
        if i.isdigit() != True and i == i.upper():
            upper = True
        if i.isdigit() != True and i == i.lower():
            lower = True
        if i.isdigit() == True:
            digit = True

    if characters == True and alpha == True and upper == True and lower == True and digit == True:
        pancakes = True
    else:
        pancakes = False

    return pancakes
    


#CODE TO RUN YOUR PROGRAM (DO NOT DELETE OR MODIFY)
if __name__ == '__main__':
    main()
