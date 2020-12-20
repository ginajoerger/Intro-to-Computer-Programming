#################################################
# HW3 - ICP Fall 2017                           #
# Exercise 1 - File Merging                     #
#################################################

def main():
    jumper = open('file1.txt', 'r')
    swimmer = open('file2.txt', 'r')

    lines = jumper.readlines()
    lines2 = swimmer.readlines()

    runner = open('file1.txt', 'w')

    joyce = ""
    fred = ""

    for i in lines2:
        joyce = joyce + i

    for v in lines:
        fred = fred + v

    runner.write(joyce + fred)

    jumper.close()
    swimmer.close()
    runner.close()


##########################################
# DO NOT MODIFY ANYTHING AFTER THIS LINE #
##########################################
if __name__ == '__main__':
    # run the main() function
    main()
