#################################################
# HW3 - ICP Fall 2017                           #
# Exercise 2 - Generate New Hire Offer Letters  #
#################################################

def main():
    jumper = open('new_hires.txt', 'r')
    swimmer = jumper.readlines()

    letter = open('offer_letter.txt', 'r')
    radical = letter.readlines()
 
    for i in swimmer:
        
        readLetter = ""
        for v in radical:
            readLetter = readLetter + v

        information = i.split(sep=',')
        applicantName = information[0]
        position = information[1]
        startDate = information[2]
        supervisorName = information[3]
        if '\n' in supervisorName:
            supervisorName = (information[3])[:-1]
        else:
            supersupervisorName = information[3]

        applicantNameSpace = applicantName.split(sep=' ')
        firstName = applicantNameSpace[0]
        lastName = applicantNameSpace[1]

        readLetter = readLetter.replace('[Applicant Name]', applicantName)
        readLetter = readLetter.replace('[Position]', position)
        readLetter = readLetter.replace('[Start Date]', startDate)
        readLetter = readLetter.replace('[Supervisor Name]', supervisorName)

        if applicantName != '[Applicant Name]':
            newFile = open('offer_letter_for_'+ firstName + '_' + lastName + '.txt', 'w')
            newFile.write(readLetter)
            newFile.close()

    jumper.close()
    letter.close()

##########################################
# DO NOT MODIFY ANYTHING AFTER THIS LINE #
##########################################
if __name__ == '__main__':
    # run the main() function
    main()
