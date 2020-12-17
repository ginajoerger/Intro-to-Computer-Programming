# HOMEWORK 0 - EXERCISE 2
# Filename: 'exercise2.py'
#
# In this file, you should write a program that:
#  1) Asks the user for a number
#  2) Prints 'odd' or 'even' depending on the number's parity
#
# Example1:
# *INPUT FROM THE USER
#  Enter a number: 17
# *PRINTED OUTPUT
#  odd
#
# Example2:
# *INPUT FROM THE USER
#  Enter a number: 4
# *PRINTED OUTPUT
#  even
# 

new_number = int(input("Please enter a number: "))

if (new_number % 2) == 0:
    print("Even")
else:
    print("Odd")

    
