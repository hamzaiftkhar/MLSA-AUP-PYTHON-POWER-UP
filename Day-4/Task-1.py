# QUESTION 01 
  
print("\n\t\tCREATING BASIC CALCULATOR\n") 
 # creating user defined functions 
def add(x,y): 
   sum=x+y 
   return sum 
  
def sub(x,y): 
   subract=x-y 
   return subract 
  
def mul(x,y): 
   multiply=x*y 
   return multiply 
  
def div(x,y): 
   division=x/y 
   return division 
  
 # asking user for numbers 
num1=int(input("\nenter first number :")) 
num2=int(input("\nenter second number :")) 
  
def calculator(): 
   choice=int(input("\nplease enter a operation you want \n1 for add\n2 for subraction\n3 for multiplication\n4 for division\n")) 
   if choice==1: 
     n= add(num1,num2) 
     print(f"the sum of numbers is {n}") 
  
   elif choice==2: 
     n=sub(num1,num2) 
     print(f"the subraction of numbers is {n}") 
  
   elif choice==3: 
     n=mul(num1,num2) 
     print(f"the multiplication of numbers is {n}") 
  
   elif choice==4: 
     n=div(num1,num2) 
     print(f"the division of numbers is {n}") 
  
   else: 
     print("invalid operation") 
  
  
  
  
calculator()