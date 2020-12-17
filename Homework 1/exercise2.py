# This code asks the user to input the number of packages they want to purchase,
# then prints the total amount of the purchase after discount.

quantity = float(input("Number of packages: ")) #inputs the number of packages
price = 49.99 #sets price to 49.99

# Next lines of code determine discounts based on quantity
# and round the numbers to two decimal places.

if quantity < 10:
    print(format(price*quantity, '.2f')) #no discount
elif quantity >= 10 and quantity <= 19:
    price = price-(price*0.1) #10% discount
    print(format(price*quantity, '.2f'))
elif quantity >= 20 and quantity <= 49:
    price = price-(price*0.2) #20% discount
    print(format(price*quantity, '.2f'))
elif quantity >= 50 and quantity <= 99:
    price = price-(price*0.3) #30% discount
    print(format(price*quantity, '.2f'))
else:
    price = price-(price*0.4) #40% discount
    print(format(price*quantity, '.2f'))
