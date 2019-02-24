# This section is included due to how Python 2.7 deals with importing text.
# It is necessary for the correct encoding of the ascii to show up and hash 
# properly.
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import hashlib
import time

# In this section we are going to store all our information.
# The PasswordList is going to contain the original passwords.
# The HashList is going to contain the Hashed versions of the passwords.
# The UpdatedList is going to contian the updated passwords, if the user enters a salted value.
PasswordList = []
HashList = []
UpdatedList = []
PasswordDictionary ={}
Hash2Crack = sys.argv[1]
Hashmaker = hashlib.sha1()
StartTime = time.time()


print("Welcome to a SHA128 Crack.")
print("Currently, we are loading some files, please wait \n")

if(len(sys.argv)>2):
    SaltedHash = sys.argv[2]
    print("You entered two hashes \n")
    print("Salt Hash: "+ str(SaltedHash)) 
    print("Hash to crack: " +str(Hash2Crack)+"\n")  

     #This section is opening CommonPasswords.txt & Saving them inside PasswordList
    filereader = open("CommonPasswords.txt","r")
    linereader = filereader.read()
    PasswordList = linereader.split()
    filereader.close()

    #This section is hashing each password in Password list & savings the hashed value inside the HashList
    for passwords in PasswordList:
    # passwords = passwords.encode('utf-8')
        Hashmaker = hashlib.sha1(passwords)
        HashList.append(Hashmaker.hexdigest())
    i = 0
     # This section is assigning the hash as the key and the original password as the value.
    for passwords in PasswordList:
        PasswordDictionary.update({HashList[i]:PasswordList[i]})
        i += 1
    
    attempts = 0

    # This section is the checking to see if the hash is present in the hashed dictionary   
    if SaltedHash in PasswordDictionary:
        attempts += 1
        print("Salted word found")
        print("Salt word: " +str(PasswordDictionary.get(SaltedHash))+"\n")
        print("Now we are going to add the salt word to our dictionary and find the real password")
        SaltedWord = PasswordDictionary.get(SaltedHash)
       
        for passwords in PasswordList:
            UpdatedList.append(SaltedWord+passwords)
       # This section is clearing the original hashlist and the dictionary. We have to repopulate those 
       # with the new corrected passwords.

        
        PasswordDictionary.clear()
        del HashList [:]
        #HashList.clear()

        for passwords in UpdatedList:
           Hashmaker = hashlib.sha1(passwords)
           HashList.append(Hashmaker.hexdigest())
        
        i = 0

        for x in UpdatedList:
            PasswordDictionary.update({HashList[i]:UpdatedList[i]})
            i += 1

        attempts = 0
        if Hash2Crack in PasswordDictionary:
            attempts += 1
            EndTime = time.time()-StartTime
            print("Password found")
            print("Original Password: " + str(PasswordDictionary.get(Hash2Crack)))     
            print("Total Time: " +str(EndTime))
            print("Total Attempts: "+str(attempts))
        else: 
            attempts += 1
            print("Password not found")
            EndTime = time.time()-StartTime
            print("Total Time: " +str(EndTime))
            print("Total Attempts: "+str(attempts))

    else:
        attempts += 1
        print("Salted word not found. Password is uncommon") 
        EndTime = time.time()-StartTime
        print("Total Time: " +str(EndTime))   
        print("Total Attempts: "+str(attempts))


else:
    print("The hash you entered was: "+str(Hash2Crack))

    #This section is opening CommonPasswords.txt & Saving them inside PasswordList
    filereader = open("CommonPasswords.txt","r")
    linereader = filereader.read()
    PasswordList = linereader.split()
    filereader.close()

    #This section is hashing each password in Password list & savings the hashed value inside the HashList
    for passwords in PasswordList:
    # passwords = passwords.encode('utf-8')
        Hashmaker = hashlib.sha1(passwords)
        HashList.append(Hashmaker.hexdigest())

    i = 0
    # This section is assigning the hash as the key and the original password as the value.
    for passwords in PasswordList:
        PasswordDictionary.update({HashList[i]:PasswordList[i]})
        i += 1
    attempts = 0    
    # This section is the checking to see if the hash is present in the hashed dictionary   
    
    if Hash2Crack in PasswordDictionary:
        attempts += 1
        print("Password found")
        print("Original Password: " +str(PasswordDictionary.get(Hash2Crack)))
        EndTime = time.time()-StartTime
        print("Total Time: " +str(EndTime))
        print("Total Attempts: "+str(attempts))
    else:
        print("Password not found. Password is uncommon")   
        EndTime = time.time()-StartTime
        print("Total Time: " +str(EndTime))
        print("Total Attempts: "+str(attempts))