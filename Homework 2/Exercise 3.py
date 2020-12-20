def main():
   usernames = []
   count = 0
   while count < 5:
      usernames.append(input("username: "))
      count += 1
   print(usernames)

   clean_userlist(usernames)

   print(clean_userlist(usernames))

def clean_userlist(usernames): 
   newList = usernames * 1
   for i in usernames:
      if "c" in i or "g" in i or "z" in i or "C" in i or "G" in i or "Z" in i:
         newList.remove(i)
   return newList
            



#CODE TO RUN YOUR PROGRAM (DO NOT DELETE OR MODIFY)
if __name__ == '__main__':
    main()
