from csv import *

from random import randint 

from termcolor import colored, cprint



def isPrime(numberUpTo):
    
    """Nat Lowis
    This will see whether it is prime or not
    Input- Number to check
    Output- Whether it is prime True or False"""
    
    if numberUpTo == 0:     #1 and 0 will come out as prime so they're here to show they are not prime
        return False
    elif numberUpTo == 1:
        return False
    elif numberUpTo == 2:
        return True
        
    integerStr = str(numberUpTo)
    
    if numberUpTo > 20:         #Uses idea that a prime must end in 1,3,7 or 9
        if integerStr[-1] != "1" and integerStr[-1] != "3" and integerStr[-1] != "7" and integerStr[-1] != "9":
            return False
    
    halfOfIt = numberUpTo ** 0.5        #Uses idea that only number must have factors below square root.  Any other above must be multiplied by ones below.
    if numberUpTo % 2 == 0:
        return False
        
    halfOfIt = int(halfOfIt)
 
    
    prime = True
    for number in range(2, halfOfIt):     #Checks every number up to the number entered checking whether if it is divided by another it will leave a remainder or not.  If not we can say it is not prime
        if numberUpTo % number != 0:
            prime = True
        else:
            return False
    
    return prime

def gcd(numberOne, numberTwo):

    if numberOne > numberTwo:
        remainder = numberTwo
    else:
        remainder = numberOne

    while remainder != 0:

        if numberOne > numberTwo:
            
            #remainder = numberOne
            numberOneTemp = numberOne
            #numberOne = numberOneTemp // remainder
            numberOne = numberOneTemp % remainder
            remainder = numberOne
        else:
            #remainder = numberTwo
            numberTwoTemp = numberTwo
            #numberTwo = numberTwoTemp // remainder
            numberTwo = numberTwoTemp % remainder
            remainder = numberTwo

    return numberOne, numberTwo

def userName_maker():

    rightUserName = False

    print("Please enter the UserName you want to use.  This will be used when you recieve messages.  IT IS CASE SENSITIVE ")
    userName = input("")
    userNameDuplicate = False

    with open("MainProgram/keys.csv", mode = "rt", encoding = "utf-8") as checkUserName:

        fileReader = reader(checkUserName)

        for record in fileReader:
            if record[0] == userName:
                userNameDuplicate = True

    while userNameDuplicate == True:

        print("This has already been taken.  Please enter a new one.  IT IS CASE SENSITIVE ")
        userName = input("")

        userNameDuplicate = False

        with open("MainProgram/keys.csv", mode = "rt", encoding = "utf-8") as checkUserName:

            fileReader = reader(checkUserName)

            for record in fileReader:
                if record[0] == userName:
                    userNameDuplicate = True
            
    while rightUserName == False:
        print("Is this username correct? Y or N")
        isUserNameCorrect = input("")
        if isUserNameCorrect not in ["Y", "N", "n", "y"]:
            print("Is this username correct? Y or N")
            isUserNameCorrect = input("")
        else:
            if isUserNameCorrect in ["Y", "y"]:
                print("SAVED")
                rightUserName = True
            else:
                print("Please enter the UserName you want to use.  This will be used when you recieve messages.  IT IS CASE SENSITIVE ")
                userName = input("")
                userNameDuplicate = False

                with open("MainProgram/keys.csv", mode = "rt", encoding = "utf-8") as checkUserName:

                    fileReader = reader(checkUserName)

                    for record in fileReader:
                        if record[0] == userName:
                            userNameDuplicate = True

                while userNameDuplicate == True:

                    print("This has already been taken.  Please enter a new one.  IT IS CASE SENSITIVE ")
                    userName = input("")

                    userNameDuplicate = False

                    with open("MainProgram/keys.csv", mode = "rt", encoding = "utf-8") as checkUserName:

                        fileReader = reader(checkUserName)

                        for record in fileReader:
                            if record[0] == userName:
                                userNameDuplicate = True

    return userName
    
def key_Generator():


    print("Welcome to the RSA Cipher.  Here we make your private and public keys which you will use to encrypt and decrypt messages with.  The Username is just so the program can find the right keys to use.  It holds no data on you. \n")
    
    finished = False
    userName = userName_maker()

    print("Making Numbers for", userName)

    while finished == False:

        p = randint(1, 100)
        q = randint(1, 100)
        nLessThan127 = p * q

        while isPrime(p) != True or isPrime(q) != True or nLessThan127 <= 127:
            p = randint(1, 100)
            q = randint(1, 100)
            nLessThan127 = p * q

        phi = (p-1)*(q-1)

        e = randint(2, phi+1)

        value1, value2 = gcd(e, phi)

        value3, value4 = gcd(e, nLessThan127)    

        if value1 == 1:
            value = value1
        else:
            value = value2

        if value3 == 1:
            valueGCDN = value3
        else:
            valueGCDN = value4

        while value != 1 or isPrime(e) != True or valueGCDN != 1:
            e = randint(2, phi+1)

            value1, value2 = gcd(e, phi)

            value3, value4 = gcd(e, nLessThan127)
    

            if value1 == 1:
                value = value1
            else:
                value = value2

            if value3 == 1:
                valueGCDN = value3
            else:
                valueGCDN = value4


        modFunction = (p - 1) * (q -1)
        d = decrypt_key(e, modFunction)

        n = p*q

        cipher = encrypter(p, q, e, "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z a b c d e f g h i j k l m n o p q r s t u v w x y z", n, False) #This is the only one which works!!

        clearToUSe = decrypter(p, q, e, cipher, n, d, False)

        numbersNotDuplicate = False
        with open("MainProgram/keys.csv", mode = "rt", encoding = "utf-8") as checkingNumbers:
            readingFile = reader(checkingNumbers)

            for recordToUse in readingFile:
                recordChecking = [p, q, e, d]
                p1 = recordToUse[1]
                q1 = recordToUse[2]
                e1 = recordToUse[3]
                d1 = recordToUse[4]
                recordToCheckAgainst = [p1, q1, e1, d1]
                if recordChecking != recordToCheckAgainst:
                    numbersNotDuplicate = True

        if clearToUSe == "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z a b c d e f g h i j k l m n o p q r s t u v w x y z" and numbersNotDuplicate == True:
            finished = True



    with open("MainProgram/keys.csv", mode = "at", newline = "", encoding = "utf-8") as RewritingFile:
        newRecord = [userName, p, q, e, d]
        fileAppend = writer(RewritingFile)
        fileAppend.writerow(newRecord)



    print("You now have keys which the program will be able to work.  The best bit is all you need to remember the username of the person you want to send a message to and your username.  The program does everything else. \n")

def decrypt_key(e1, modulus):

    """Works out the decryption key
    Inputs - e and the modulus both integers
    Outputs - The decryption key"""

    d = 1           #Setting d to 1
    finished = False        #To check if we found a value for d
    while finished != True:             #We check to see if we have a value for d
        newD = e1 * d                   #Works out the remainder using the equation ed (mod modulus) = 1
        finalD = newD % modulus
        
        if finalD == 1:         #If the remainder is 1 we have a value for d!!
            finished = True
        else:
            d = d + 1


    return d

def encrypter(w, q, e, string, n1, checker):

    """Inputs - The 3 numbers and the number to be encrypted
    Outputs - The Encrypted message
    This is where the message will be encrypted"""

    if checker == True:
        print("Enter Username of the person you want to send the message to.  If you do not have one use admin.")
        userNameToUse = input("")

        isUserNameThere = False

        while isUserNameThere == False:
            with open("MainProgram/keys.csv", mode = "rt",  encoding = "utf-8") as  checkingUserName:
                fileToRead = reader(checkingUserName)

                for record in fileToRead:
                    if record[0] == userNameToUse:
                        w = int(record[1])
                        q = int(record[2])
                        e = int(record[3])

                        n1 = w * q
                        isUserNameThere = True

                if isUserNameThere == False:
                    print("The username wasn't correct.  Please try again")
                    userNameToUse = input("")

        string = input("Please enter the message to be encrypted: ")

            

    cipherText = []     #This  is where the cipher text will go

    for letter in string:           #Takes each letter in the plaintext


        m3 = ord(letter)

                #THIS NEEDS TO BE SMALLER THAN N OKAYYYYYYYY

        c1 = m3**e
        c2 = c1% n1

        cipherText.append(c2)
    

    return cipherText

def decrypter(w, q, e, cipher, n2, dToUSe, checker2):

    """Inputs - The 3 numbers and cipher text
    Outputs - The plaintext
    This will decrypt the message"""

    if checker2 == True:
        print("Enter your username so you can decrypt the message you have recieved.  Make sure it has been encrypted using your username.  If you do not have one use admin but make sure it has been encrypted using admin.")
        userNameToUse = input("")
        print("\n")

        isUserNameThere = False

        while isUserNameThere == False:
            with open("MainProgram/keys.csv", mode = "rt",  encoding = "utf-8") as  checkingUserName:
                fileToRead = reader(checkingUserName)

                for record in fileToRead:
                    if record[0] == userNameToUse:
                        w = int(record[1])
                        q = int(record[2])
                        dToUSe = int(record[4])

                        n2 = w * q
                        isUserNameThere = True

                if isUserNameThere == False:
                    print("The username wasn't correct.  Please try again")
                    userNameToUse = input("")

        cipherToChange = input("Please enter the message to be encrypted: ")
        cipher = []
        numbers = ""
        for character in cipherToChange:
            if character == ",":
                cipher.append(numbers)
                numbers = ""
            else:
                numbers = numbers + character

    clear =""       #The clear text
    for charatcer in cipher:        #Takes each letter in the cipher       

        charatcer = int(charatcer)
        m1 = charatcer ** dToUSe     #Uses the equation above to decrypt message
        m2 = m1 % n2

        
        #print(m2)

        intm2 = round(m2)

        letter = chr(intm2)

        clear = clear + letter
        
    return clear

def newUser():
    print("Have you ever used this RSA Program before? Y or N")
    used = input("")
    if used in ["NO", "No", "N", "Nope", "n", "no", "nO", "Never"]:
        key_Generator()
    
def menu():
    menuOption = input(colored("Choose an option.  \n 1. Encrypyt message \n 2. Decrypt message \n 3. What the RSA Cipher does \n Enter 1, 2 or 3 ", "blue", "on_white"))  #This will ask the user which conversion they want to do

    while menuOption not in["1", "2", "3"]:
        menuOption = input(colored("Choose an option.  \n 1. Encrypyt message \n 2. Decrypt message \n 3. What the RSA Cipher does \n Enter 1, 2 or 3 ", "red", attrs = ["blink"]))  #This will ask the user which conversion they want to do
    
    return menuOption
########################################################################################################################################################################################
    
def again():
    
    """Menu to repeat program"""
    
    againYOrN = input("Do you want to reuse the RSA Cipher? Y or N: ")
    
    while againYOrN not in["Y", "n", "N", "y"]:
        againYOrN = input("Do you want to rerun the RSA Cipher? Y or N: ")  #This will ask the user which conversion they want to do
        
    if againYOrN in ["Y", "y"]:
        
        return True
        
    else: 
        exit()
########################################################################################################################################################################################

newUser()

looper = True
while looper ==True:        #Looper which keeps on working
    
    menuOption = menu() #menu
    
    if menuOption == "1":       #Traditional Game
        cipher = encrypter(None, None, None, None, None, True) #This is the only one which works!!
        print(cipher)       #Work out how to do this
        clearText = ""
        for number in cipher:
            clearText = clearText + str(number) + ","

        print("This is the encrypted message.  Copy the whole message including the stray comma!")
        print(clearText)
    elif menuOption == "2":     

        message = decrypter(None, None, None, None, None, None, True)
        print("The message reads:", message)
    
    else:
        print("The RSA Cipher was made in 1977 and is named after the three people who made it:  Ron Rivest, Adi Shamir, and Leonard Adleman.  It was the first assymetric key cipher meaning you need different numbers to make and break the cipher.  It is at the moment impossible to break as when using large enough numbers you cannot break the numbers back into the prime numbers.  It uses modular mathematics which is the maths of using remainders.  All you have to do is enter the username of the person you want to send the message to and then let them decrypt it \n \n")
    

    looper = again()



