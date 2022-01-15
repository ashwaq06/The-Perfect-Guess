import random
number= random.randint(1,1000)
attempt= 1
guess= int(input("Guess the number:"))
while(True):

  if(guess>number):
    guess= int(input("looks like you guessed a higher number please Guess the number again: "))
    attempt+= 1

  if(guess<number):
     guess= int(input("looks like you guessed a lower number please Guess the number again: "))
     attempt+= 1

  else:
    print(f"Hurray,You Guessed it right in {attempt} attempts")
    break

 