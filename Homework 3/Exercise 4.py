#################################################
# HW3 - ICP Fall 2017                           #
# Exercise 4 - PM2.5                            #
#################################################

def build_dict(fileName):
    file = open(fileName, 'r')

    readFile = file.readlines()
    joyce = {}

    for i in readFile[1:]:
        split = i.split(sep=' ')
        firstSplit = split[0].split(sep=',')
        secondSplit = split[1].split(sep=',')

        try:
            if int(secondSplit[1])>int(joyce[firstSplit[2]]):
                joyce[firstSplit[2]] = int(secondSplit[1])
        except:
            joyce[firstSplit[2]] = int(secondSplit[1])

    return joyce

def cnt_smog_days(dictionary):
    counter = 0
    for i in dictionary:
        if dictionary[i] >= 80:
            counter = counter + 1
        
    return counter           

def cnt_clear_days(secondDictionary):
    counter = 0
    for i in secondDictionary:
        if secondDictionary[i] <= 40 and secondDictionary[i] >= 0:
            counter = counter + 1

    return counter 

def cnt_unavailable_days(thirdDictionary):
    counter = 0
    for i in thirdDictionary:
        if thirdDictionary[i] == -999:
            counter = counter + 1

    return counter       

def main():
    first = build_dict("Shanghai_2016_HourlyPM25.txt")
    smog = cnt_smog_days(first)
    clear = cnt_clear_days(first)
    unavailable = cnt_unavailable_days(first)
    print("Number of smog days:", smog)
    print("Number of clear days:", clear)
    print("Number of days with no data:", unavailable)
    


##########################################
# DO NOT MODIFY ANYTHING AFTER THIS LINE #
##########################################
if __name__ == '__main__':
    # run the main() function
    main()
