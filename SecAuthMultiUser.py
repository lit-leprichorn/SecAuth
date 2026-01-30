#coded BY HAND by lit-leprichorn  in 2026, thursday 29th january hell yeah 
#I THINK THIS ACTUALLY WORKS WTH WHAT OMG
#this is for logic and init.needed to work.pls dont move tjis

import random #DONT delete
import math #here just incase.
import time #same here, dont delete
attemps = 3# means attempts,but too late now lol. edit for more chances.
userfa = 0
accounts = {}
bannedusers = {}

# high chance only time gets used lol

right = int(3 * 2 / 3 + 4 -1) # semi obfuscated,causing you to use your brain lol
setflag = False #yeah false okay
twofa = random.randint(1362, 326151072) #generate before hand beacause its cleaner looking.
sectwofa = twofa

#pswrd = "null" depricated due to THE REAL system..wow.

loginor = "none"
found = False
loadmode = 0
usrname = "nul"
banned = 0

#bantest = True
#next itteration: "secret" hardcoded user with a custom dev pannel. and ban system

# does right even get used anymore??? i dont wanna comment it out and risk it lol does


#the stuff below in the login and 2FA script.
print("Welcome to SecAuth secure systems.")
time.sleep(2)
print("Starting SecAuth systems ... ") # let me tell you a secret, this doesnt do anything hehehe
print("                                                    ")
time.sleep(0.8)
# user controll for making a new account or signing in.
loginor = input("Would you like to create an account or sign in?")
if loginor in ["new", "create", "make","1"]:    # should run if it finds ANY make, create blah blah.so this is ideal i think?
    accname = input("Create your User name.")
    time.sleep(1)
    accpass = input("please create an password .")# numbers only... liar liar. we aint in 1572. i can do leters now hehe
    time.sleep(2)
    print("Saving details ... ")# liar this happens after you say it.
    with open("UserAccountData.txt", "a") as b:
        b.write(f"{accname}:{accpass}\n")# this pust your account name and password, in raw text, i a file stored locally... very smart design (no im not encrypting it!)
        time.sleep(0.7)
        print("User details saved!")
        exit()
elif loginor in [ "sign in","login","load","sign", "2"]: #should run if it sees any: load,login ect.
    print("You have selected: Log in!")#really???? who knew that
    loadmode = 1
    pass

#if bantest == True:
#    with open("BannedUsers.txt", "a") as bannedg:
#        bannedg.write(f":{usrname}\n")



#the huge gap in second print is to leave a gap in the output,showing "Starting SecAuth ... (big gap) whats the password blah blah tk" why have i not moved this
#line 46 is clearly better than line 45. i dont yap

# account and password loading goes here.
with open("UserAccountData.txt", "r") as z:
    for line in z:
        loaded_user, loaded_pass = line.strip().split(":")#line.strip.split,puts the line into {"Username", "password"} the line,then splits it at the poing eg: ":"
        accounts[loaded_user] = loaded_pass# stores user password as "passworsd" isnide the table accounts[loaded_user]

#loaded_user = "test"
#loaded_pass = 1234 #this is for testing account login system

#ban system
#with open("BannedUsers.txt" "r") as banload:
#    for line in banload:
#        blankdata, banacc = line.strip().split(":")
#        bannedusers[blankdata] = banacc
#ban system cant find the file... ven th it exists. fix that later
        
#print(bannedusers)


while attemps > 0 and setflag == False and loadmode == 1 and banned == 0:
    usrname = input("What is your user name?")
    try:
        pswrd = (input("Whats your password?")) # just gonna put account after😭
    except:
        print("Invalid password. numbers only!") # still takes an attempt because i say so lol
        # the try and except allow user to input text, and not crash the python lol.
        attemps = attemps - 1
        #print(accounts[loaded_user], loaded_user, loaded_pass ) debug cus it wasnt working... turns out it was caused by the stupid no intigers and tring rule . ahahahauahahu
    if usrname in accounts and accounts[usrname] and pswrd == accounts[usrname]:# this compares user imputted user name to the table of accounts (tyler, password ect) and sees if the password matches, if so it then logs in.
        print("You have logged in!")
        found = True
        setflag = True
    else:
        attemps = attemps - 1
        print("Wrong information! you have: ", attemps, "trys remaining.")
if found == True:
    print("Welcome back",usrname)
        
    
    if pswrd == accounts[usrname]: # means that if the password is equal to a pasword isnide our list of users and passwords, its happy and logs in.
        print("Correct password!")
        setflag = True
        print(twofa, "is your one time 2FA code.")
        userfa = int(input("Please confirm your 2FA backup code?"))# DESIGNED to NOT be initialised before password is right.as the program exits and the script uses a flag looking for this as 2fa and True flags.
    else:
        attemps = attemps - 1
        print("Wrong password.", attemps, "trys left.")
        



# ban handling should start before ALL error handling.

#if bantest == True:
#    with open("BannedUsers.txt", "a") as bannedg:
#        bannedg.write(f"{usrname}\n")



# wrong password error handling
if attemps == 0:
    print(" Due to suspicious activity, login has been temporarily locked.")
    time.sleep(1)
    print("Security event has been logged.")
    print("User Session ID:", random.randint(10000, 99999999))
    with open("UserforgorPassword.txt", "a") as t:
        t.write(f"User {usrname} has failed password check. Error code: 222. time: {time.ctime()}\n")#this logs the users failed attemps and saves to a file, set to "a" to show the ammount of times this has happened.
        exit()
# not putting a valid option for loginor
if loadmode == 0:
    print("Sorry, ", loginor," is not an available option. The program will now close.")
    print("Error code:", random.randint(100, 789), "User put an invalid option.") # fake error code for if the user is an idiot and puts something like "p"
    with open("UserforgorPassword.txt", "a") as stupiduser:
        stupiduser.write(f"DefaultUser has put an invalid option in the account options time: {time.ctime()}\n")

#showing this cus im not guessing it
#since this is just a demo,the password is 5: GUESS WHAT.NO LONGER A DEMO HOLY also... this is like 40 lines away from what its suppost to comment...

#this line is used for 2fa handling.
if userfa == twofa:
    pass #literaly just here so i can get thw if user fa is wrong.
else:
    userfa = 2
    print("User 2FA failed. system will now exit.")
    time.sleep(2)
    print("SecAuth.state = state.off")# looks like a dev output,then the other checks fail and the program exits.
    with open("UserforgorPassword.txt","a") as v:
        v.write(f"User {usrname} failed 2FA secure check. {time.ctime()}\n")
        exit() # just stops the code...that why its called exit😭🙏


# failed login logic yeah... your a couple 50 lines off here mate....


 #use value right to hide the actual password,instead of puting it in plain text lol... 100 lines away from home
  
  #the big one that writes state to file logic.
  
if setflag == True and userfa == twofa and attemps <= 3: #tripple layered auth checks,stops any bypasses or glitches from user end.
    print("User Verified!") # here just to make sure it works and detects the value
    with open("ConfirmedUserState.txt","a") as f:
        f.write(f"Verified User! {usrname} {time.ctime()}\n")
        #f.close() dont need u any more bozo

# ban system used to be here. ban detection would be at top, running beofore all main code. for imediate banning
#if bantest == True:
 #   with open("BannedUsers.txt", "a") as bannedg:
 #       bannedg.write(f"{usrname}\n")

# 
#
#
#
#jon was here
#typing on mobile is painfull😭😭🌝🌚