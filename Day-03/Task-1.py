# QUESTION 01

import random
print("\n\t\tGUESSIMG CORRECT NUMBER\n")
rand_num=random.randint(0,100)
# print(rand_num)
count=0
num=int(input("\nplease guess a number\n"))
# print (num)
if rand_num==num:
  print("\ncongrats \nyou guessed a right number:)")
  count+=1
  print(f"you guess the correct number in {count} attempt")
else:
  while rand_num !=num:
    count+=1
    num=int(input("\nplease guess  again\n"))
    if rand_num==num:
      print("\ncongrats \nyou guessed a right number:)")
      count+=1
      print(f"you guess the correct number in {count}th attempt")
    
