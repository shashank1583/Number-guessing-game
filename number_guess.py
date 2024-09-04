import random
n = random.randrange(1,10)
guess = int(input("Enter any number ranging from 1 to 10: "))

#no of guesses
g=1

while n!= guess:
    #check whether the guessed number is above 0 and below 10
    while guess<= 0 or guess >10:
        guess=int(input("Please type a number larger than 0 and less than 10: "))
    if guess < n:
        print("You were below the number!")
        guess = int(input("Enter number again: "))
    elif guess > n:
        print("You were above the number!")
        guess = int(input("Enter number again: "))
    else:
      break
    g+=1
    
#printing result
print("------------------------------------")
print("you guessed it right!!")
print("you guessed the number in "+str(g)+" guesses!")
print("------------------------------------")
