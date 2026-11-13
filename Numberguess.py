import random
a = random.randint(0,100)

b = int(input("Guess the nummber from 0-100 :"))
while(b!=a):

    print("Oh nooo!!!!!")
    print("The number guessed in wrong")

    if a > b:
        print("The number is greater than previously guessed number")

    else:
        print("The number is lesser than previouly guessed number")

    b = int(input("Enter the guessed number again : "))


print("CONGRATS!!!!!!")
print("The number guessed is correct")


