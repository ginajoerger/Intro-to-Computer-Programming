# Homework 2

## Exercise 1 - Draw an Hourglass

Write a program (in the main() in the file exercise1.py) which asks the user to enter a positive
integer N and then draws an hourglass of the corresponding size ( 2 * N - 1 lines).
The hourglass is obtained by drawing lines containing spaces and stars.

## Exercise 2 - Rock, Paper, Scissors Game

The program should work as follows:

1. When the program begins, a random choice of rock, paper, scissors is generated as
computer’s choice (but do not display the computer’s choice yet)

2. The user inputs his or her choice: rock , paper , scissors (upper or lower cases will not
matter)

3. If the user inputs another string than the 3 choices (again, upper or lower cases will not
matter), the program should ask the user to input again

4. The computer’s choice is then displayed and a message is displayed ( you win or
you lose ). If the user makes the same choice as the computer, the game must be played
again to determine the winner

5. If 3 games were played without a winner, output draw

## Exercise 3 - Remove Special Usernames

Write a function called clean userlist (in the file exercise3.py) that:

1. Takes a list as input argument, knowing that each element in the list is a string representing a username in the system
2. Returns a new list where all the usernames that contain c , g or z were removed (the
usernames with C , G or Z should also be removed)

Then, write a program (in the main() in the file exercise3.py) that:

1. asks the user to input 5 usernames (only alphanumeric characters will be input, no space,
no underscore, . . . ) and stores them into a list
2. prints out the list
3. calls clean userlist function to clean the list
4. prints out the cleaned list

## Exercise 4 - Valid Username

Write a function called valid username (in the file exercise4.py) that:

1. takes one string, and one list as input arguments
2. checks if this username respects the rules (see below)
3. prints out a message ( Valid , Invalid or User Name Exists )
4. returns a Boolean value representing if the provided string (input argument) is a valid
username or not

Then, write a program (in the main() in the file exercise4.py) that:

• initialize a userList with the following value:
userList = [['suny1', 'pwd1ddf'], ['superSS', 'pwd2yzw'], ['likeA', 'pwd3ppq']]
• asks the user to input a username
• calls valid username function with the username and the userList as arguments
• prints out the returned value from the function

## Exercise 5 - Valid Password

Write a function called valid password (in the file exercise5.py) that:

1. takes one string as input argument
2. checks if this password respects the rules (see below)
3. prints out a message ( Valid or Invalid )
4. returns a Boolean value representing if the provided string (input argument) is a valid
password or not

The printed out message/returned value will be:
• Invalid / False if the password is not correct
• Valid / True if all the rules are respected

Then, write a program (in the main() in the file exercise5.py) that:
• asks the user to input a password
• calls valid password function with the password as an argument
• prints out the returned value from the function
