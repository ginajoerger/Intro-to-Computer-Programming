# This code asks the user to input a year, the prints the message "Leap Year"
# and "Not Leap Year" based on the result of the program. Then, if applicable,
# it prints the message "World Cup year" or "Euro Cup year" on a second line.

year = int(input("Year: ")) #input a year

if year % 4 == 0 and year % 400 == 0: #requirements for a leap year
    print("Leap year")
elif year % 100 == 0: #does not fit requirements for a leap year
    print("Not leap year")
else:
    print("Not leap year")
    
if year >= 1950 and (year-1950) % 4 == 0: #requirements for world cup year
    print("World Cup year")
if year >= 1960 and (year-1960) % 4 == 0: #requirements for euro cup year
    print("Euro Cup year")

    
