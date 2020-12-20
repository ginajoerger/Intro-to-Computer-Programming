def main():
    userList = [['suny1', 'pwd1ddf'], ['superSS', 'pwd2yzw'], ['likeA', 'pwd3ppq']]
    string = input("Enter: ")
    list1=[]
    for a in range(3):
        list1.append(userList[a][0])
    print(valid_username(string, list1))
    
    
def valid_username(string, list0):
    characters = True
    alpha = True
    digit = True
    pancake = True
    user = False
    if len(string) <= 3:
        characters = False
    if string.isalnum() != True:
        alpha = False
    if string[0].isdigit():
        digit = False

    if string in list0:       
                user = True
              
    #Invalid
    if user == True:
        pancake = False
        print('User Name Exists')
    elif user == False and (characters == False or alpha == False or\
         digit == False):
        pancake = False
        print('Invalid')
    elif user == False and characters == True and alpha == True and\
                digit == True:
        pancake == True
        print('Valid')

    return pancake
        
    



#CODE TO RUN YOUR PROGRAM (DO NOT DELETE OR MODIFY)
if __name__ == '__main__':
    main()
