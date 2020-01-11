##########################################################################
# 2019 Summer Challenges 
# Game: Guess the Number
#      User selects option 1 - Computer guess your number
#      User selects option 2 - You guess computer number
# Uses: Ramdom, round, while, if, else, float, int, input, print, etc
##########################################################################
import random
def OptionComputerGuess():
    ####TODO: DELETE and Write your code here...####
    print("You selected: Computer guess your number")
    enterC = input("Input your number")
    enterC1 = float(enterC)
    max = 50
    min = 1
    gurgomflop = 1
    while gurgomflop!=8:
        myRandomNumber = random.randint(min,max)
        myRandomNumber1 = float(myRandomNumber)
        print (myRandomNumber1)
        answer = input("(g=greater l=less c=correct)")
        if answer == ("g"):
            min = myRandomNumber1 + 1
        elif answer == ("l"):
            max = myRandomNumber1 - 1
        elif answer == ("c"):
            print ("Yaaaaay! I won!")
            gurgomflop = 8
        else:
            print ("error")
            gurgomflop = 8
    enterC = input("<<Enter>>")


   
def OptionYouGuess():
    print("You selected: You guess computer number")
    myRandomNumber = random.randint(1,50)
    enter1 = -1.0
    while enter1!=myRandomNumber:
        enter = input("is it greater or less than ")
        enter1 = float(enter)
        if enter1>myRandomNumber:
            print("My number is less")
        elif enter1<myRandomNumber:
            print("My number is greater")
        else:
            print("You have guessed my number")
    enterC = input("<<Enter>>")

def OptionInvalid():
    print("Invalid number!!! Please use 0,1,2 or 3")
    enterI = input("<<Enter>>")

#--- Helpfull functions: these "may" be usefull in your code ---# 
def HelpfullFunctions():
    print (">>HelpfullFunctions:")
    # Generates a random integer -  from 1 to 50, endpoints included 
    myRamdomNumber  = random.randint(1, 50)
    # Rourd decimal numbers (float)
    floatValue = input("Type a decimal number - e.g. 7.3 : ")
    floatNumber = float(floatValue)
    myRoundedNumber= round(floatNumber)
    print (">>>> myRamdomNumber: ",myRamdomNumber, " myRoundedNumber: ",myRoundedNumber)
    keyValue = input("<< Press ENTER >>")

#--- This is the main program, you may use  any function defined above ---# 
# We use the following "while" and "clearscreen()" to create a menu of options.
selectedOption="-1"
while(selectedOption!="0"):   
    #clearScreen()
    print("---------------------------------------------------------")
    print("---- Game: Guess the Number ---")
    print("Type desired option number and press <<Enter>>:")
    print("1 - Computer guess your number")
    print("2 - You guess computer number")
    print("3 - To run HelpfullFunctions() ")
    print("0 - Exit program")
    print("")
    selectedOption = input("Option? ")
    if selectedOption=="1":
        OptionComputerGuess()
    elif selectedOption=="2":
        OptionYouGuess()
    elif selectedOption=="3":
        HelpfullFunctions()
    elif selectedOption=="0":
        print("Thanks for Playing! See You!")
        exit()
    else:
         OptionInvalid()
    print("---------------------------------------------------------")