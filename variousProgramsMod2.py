#program created by elijah gonzalez. contains various programs inside of one.
#will explain when we get to each one, keep reading. file name is
#variousProgramsMod2

#program 1: guess number 1-10.

#import random to genreate a number on the next line
import random

#set our secret to the randomly generated number between 1 and 10
secret = random.randint(1,10)

#define guess as 0, which is impossible for the secret to equal, as its only
#1-10.
guess = 0

#tell the user to guess once
print("Guess the number!")

#while the secret has not been guessed, the program will loop until it is.
while guess != secret:

    #tell the user to guess
    guess = int(input("Enter your guess: "))

    #if the guess is greater than the secret, tell them too high
    if guess > secret:
        print("Too high!")

    #do the same here, but instead if its less than and too low
    elif guess < secret:
        print("Too low!")

    #if it is neither, it must be the correct number, so we tell the user
    #they got it, and we print the secret as well to confirm.
    else:
        print("Just right! Number was:",secret)


#program 2: green and smalls. the program takes various if statements to
#determine what the object is. the objects are pea, cherry, watermelon, and
#pumpkin

#this is a spacing line.
print()

#we set our variables here.
green = True
small = True

#done is for the while loop.
done = False

#once done is set to true, the loop ends.
while done != True:
    
    #if the object is both green and small, it must be a pea, so we print it.
    if green == True and small == True:
        print("pea")

        #we then set green to false.
        green = False

    #if the object is not green but small, it must be a cherry. so we print it
    elif green == False and small == True:
        print("cherry")

        #we change it again.
        green = True
        small = False
    #if the object is green but not small, it must be a watermelon. print again
    elif green == True and small == False:
        print("watermelon")

        #set both to false
        green = False
        small = False

    #if the object is neither green or small, it is a pumpkin. so we print it out
    #and set done to true so that the while loop may end.
    elif green == False and small == False:
        print("pumpkin")
        done = True
        
#this is a spacer.
print()

#program 3: print a list out.

#set a list, to 3,2,1, and 0. 
numlist = [3,2,1,0]

#for the item in the list, print the number, then go to the number in the list.
for n in numlist:
    print(n)

#spacer
print()

#program 4: create a loop with guess me as 7, number as 1. we have a var 
#we use called numdone as well to tell us when the loop is... done.
#we set guess_me to 7, number 1 to, and numdone to false.
guess_me = 7
number = 1
numdone = False

#while numdone is false, the loop continues.
while numdone == False:
    
    #if the number is less than guess_me, we tell the user it is too low.
    if number < guess_me:
        print("Too low")
        
        #then we add number to itself +1
        number = number+1
        
    #if number is equal to guess me, we found it. so we tell the user and
    #set numdone to true to end the loop, as numdone no longer is false.
    elif number == guess_me:
        print("Found it!")
        numdone = True
        
    #if it ever goes higher than guess_me, we print oops, as something went
    #wrong. but we should never see this.
    elif number > guess_me:
        print("oops")
#then we print loop finished 
print("Loop finished")

print()

#program five. same as above, but instead we use it in a range. i used 1-10,
#so that it counts up from 1 to 10 instead of starting at 0.

#we set our variables
guess_me = 5
number = 1

#for number in the range of 1,10, we go up the range starting from 1 to 10.
for number in range(1,10):
    
    #if number is less than guess_me, which is 5, we say too low.
    if number < guess_me:
        print("Too low")
        
    #once its equal, we print found it! so we print that.
    elif number == guess_me:
        print("Found it!")
        
    #once we count again, number is at  6, which is over 5, so we just say oops and
    #and then exit the loop.
    else:
        print("oops")
        exit()



  

        
