# HOMEWORK 0 - EXERCISE 1
# Filename: 'exercise1.py'
#
# In this file, you should write a program that:
#  1) Asks the user for a family name
#  2) Asks the user for a given name
#  3) Prints the sentence 'Hello <given name> <family name> !!!'
#
# Example:
# *INPUTS FROM THE USER
#  Family name: Corcolle
#  Given name: Romain
# *PRINTED OUTPUT
#  Hello Romain Corcolle !!!
# 

family_name = str(input("Please enter your family name: "))
given_name = str(input("Please enter your given name: "))

print("Hello " + given_name + " " + family_name + " !!!")
