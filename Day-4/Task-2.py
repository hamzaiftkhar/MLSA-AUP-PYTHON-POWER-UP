# QUESTION 02 
  
print("\n\t\tWORD FREQUENCY COUNTER\n") 
  
def frequency(): 
   string=input("please enetr a string :\n") 
   list=string.split() 
   # print(list) 
  
   # empy dictionary 
   dic={} 
   for i in list: 
     if i not in dic.keys(): 
       dic[i]=1 
  
   dic[i]=dic[i]+1 
   print("\n",dic) 
frequency()  