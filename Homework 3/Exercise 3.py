#################################################
# HW3 - ICP Fall 2017                           #
# Exercise 3 - Top Tourist Attractions in China #
#################################################

def build_attraction_dict(fileName):
    file = open(fileName, 'r')
    
    readFile = file.readlines()
    joyce = {}

    for i in readFile:
        split = i.split(sep=',')
        attractionName = split[1]
        province = split[0]
        
        if '\n' in i:
            attractionName = (split[1])[:-1]
        else:
            attractionName = split[1]

        joyce[attractionName] = province

    file.close()

    return joyce
 
def add_attraction(dictionary):
    attractionName = input("Input a new attraction: ")
    province = input("Input the province: ")

    dictionary[attractionName] = province

def build_province_attraction_dict(secondDictionary):
    province = secondDictionary.values()
    attractionName = secondDictionary.keys()

    wayne = {}

    for i in province:
        attraction = []
        for v in attractionName:
            a = secondDictionary[v]
            if a == i:
                attraction.append(v)
                wayne[i] = attraction

    return wayne

def most_attractions(thirdDictionary):
    provinceNames = thirdDictionary.keys()
    jumper = []

    for i in provinceNames:
        if len(thirdDictionary[i]) >= 3:
            jumper.append(i)

    set1 = set(jumper)

    return set1

def main():
    step1 = build_attraction_dict('top_tourist_attractions.txt')
    step2 = add_attraction(step1)
    step3 = build_province_attraction_dict(step1)
    step4 = most_attractions(step3)
    print("\nProvinces with at least 3 attractions:")
    for i in step4:
        print(i)

##########################################
# DO NOT MODIFY ANYTHING AFTER THIS LINE #
##########################################
if __name__ == '__main__':
    # run the main() function
    main()
