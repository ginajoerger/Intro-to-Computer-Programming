# The main purpose of this code is to print out a sequence of numbers based on
# a set of rules, and for the sequence to end once the number reaches 1.
# In the end, there must also be a sum of all the numbers produced in the sequence.

prompt = int(input("Input a number: ")) #Input a number
sum = prompt 

print (prompt) #Must print the origional number


if prompt < 0:
    print("Error - Execution Failed.") #To make sure number submitted is positive
else:
    while prompt != 1: #stops once loop reaches 1
        if prompt % 2 == 0: #determines whether it is even or not
            even = prompt // 2 #divides by 2
            print (even)
            prompt = even
            sum += even #Adds sum onto new figure
        else:
            odd = 3 * (prompt) + 1 #follows sequence rule for odd numbers
            print (odd)
            prompt = odd
            sum += odd #Adds sum onto new figure

print (sum) #Entire sequence ends with one final sum of all numbers



    

            
