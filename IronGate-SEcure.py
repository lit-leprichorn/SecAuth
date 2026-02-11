import time
import random
import os # for boot up chime in next version
UsrData = {}
#all the functions and subprograms required to run


def GetUsers():
    global UsrPass
    with open("UserData1.txt","r") as getusr:
        for line in getusr:
            UsrName, UsrPass = line.strip().split(":")
            UsrData[UsrName] = UsrPass

def login():
    global loginin
    loginin = 1 #1 means logging in
    Attempts = 3
    print("You have selected: Login.")
    while loginin == 1 and Attempts > 0:
        NameInput = input("What is your username?")
        PassInput = input("What is your password?")
        if NameInput in UsrData and UsrData[NameInput] == PassInput:
            loginin = 0 #means user sucsesfully logged in.
            print(NameInput, "Has signed in.")
        else:
            print("Wrong infornation!")
            Attempts = Attempts - 1
            

def NewAccMaker():
    loginin = 2 # 2 means making new account.
    rank = "user"#Deault rank
    print("You have selected: Create account!")
    SelName = input("Create an user name.")
    SelPass = input("Create an password.")
    #Compare = int(input("What is user rank code? (222)"))
    #if Compare == 1234:# default test password.change later on.
        #rank = "admin"#special rank
    with open("UserData1.txt", "a") as Save:
        Save.write(f"{SelName}:{SelPass}\n")
        print("Saving data ... ")
        time.sleep(1)
        print("Data saved!")
        time.sleep(2)
        exit()
    



def SignInErr():
    print("Sorry, ", SignOrNew, "is not a valid option!")

#call all functions to start the stuff
GetUsers() #COMMENT FOR 1st run of code

print("IrongGate loading . . .")
time.sleep(1)
print("Starting systems . . .")
time.sleep(2)
print(random.randint(1413, 2872), " Processes started.")

SignOrNew = input("Would you like to sign in or create a new account?")
if SignOrNew.lower() in ["sign in", "signin", "load", "log in", "login", "2"]:
    login()
    
elif SignOrNew.lower() in ["new", "account maker", "1", "create", "new acc", "make"]:
    NewAccMaker()
else:
    SignInErr()
    print("System Error! Err code: " ,random.randint(241, 999), " User is an IDIOT!!")
    exit()