import random
def cat():
    randomResult = random.randint(0,2)
    if randomResult == 0:
        result = "rock"
    elif randomResult == 1:
        result = "paper"
    elif randomResult == 2:
        result = "scissors"
    return result

def main():
    

    drawCounter = 1
    result = cat()
    
    userInput = (str(input("you: "))).lower()
    while userInput != 'rock' and userInput != 'paper' and userInput != 'scissors':
        userInput = (str(input("you: "))).lower()

    print("computer: ", result)

    if userInput == result:
        drawCounter += 1
    elif userInput == 'rock' and result == 'paper':
        print("you lose")
    elif userInput == 'rock' and result == 'scissors':
        print("you win")
    elif userInput == 'paper' and result == 'rock':
        print("you win")
    elif userInput == 'paper' and result == 'scissors':
        print("you lose")
    elif userInput == 'scissors' and result == 'rock':
        print("you lose")
    elif userInput == 'scissors' and result == 'paper':
        print("you win")

    if drawCounter == 2:
        result = cat()
    
        userInput = (str(input("you: "))).lower()
        while userInput != 'rock' and userInput != 'paper' and userInput != 'scissors':
            userInput = (str(input("you: "))).lower()

        print("computer: ", result)

        if userInput == result:
            drawCounter += 1
        elif userInput == 'rock' and result == 'paper':
            print("you lose")
        elif userInput == 'rock' and result == 'scissors':
            print("you win")
        elif userInput == 'paper' and result == 'rock':
            print("you win")
        elif userInput == 'paper' and result == 'scissors':
            print("you lose")
        elif userInput == 'scissors' and result == 'rock':
            print("you lose")
        elif userInput == 'scissors' and result == 'paper':
            print("you win")

    if drawCounter == 3:
        result = cat()
    
        userInput = (str(input("you: "))).lower()
        while userInput != 'rock' and userInput != 'paper' and userInput != 'scissors':
            userInput = (str(input("you: "))).lower()

        print("computer: ", result)

        if userInput == result:
            print('draw')
        elif userInput == 'rock' and result == 'paper':
            print("you lose")
        elif userInput == 'rock' and result == 'scissors':
            print("you win")
        elif userInput == 'paper' and result == 'rock':
            print("you win")
        elif userInput == 'paper' and result == 'scissors':
            print("you lose")
        elif userInput == 'scissors' and result == 'rock':
            print("you lose")
        elif userInput == 'scissors' and result == 'paper':
            print("you win")


#CODE TO RUN YOUR PROGRAM (DO NOT DELETE OR MODIFY)
if __name__ == '__main__':
    main()

