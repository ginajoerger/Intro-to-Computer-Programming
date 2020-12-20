def main():
       n = int(input("Please enter a positive integer: "))
       lines = 2 * n - 1
       space = 0
       stars = 0
       tester = (lines//2)
       for i in range(tester):
              stars = ("*" * lines)
              actualSpace = (" " * space)
              triangle = actualSpace + stars
              print(triangle)
              space = space + 1
              lines = lines - 2
       for x in range(tester + 1):
              stars = ("*" * lines)
              actualSpace = (" " * space)
              triangle = actualSpace + stars
              print(triangle)
              space = space - 1
              lines = lines + 2

    
#CODE TO RUN YOUR PROGRAM (DO NOT DELETE OR MODIFY)
if __name__ == '__main__':
    main()
