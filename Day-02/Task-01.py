""" Question-1:
Lists and Tuples You have been given the following data:

temperatures = [25, 30, 27, 22, 28, 33, 29] 
days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday') 

a) Create a new list containing the temperature and day pairs as tuples. 
b) Find the maximum temperature from the list and print it along with the corresponding day. 
c) Calculate and print the average temperature."""

# Answer-1:

# a) Create a new list containing the temperature and day pairs as tuples.
temperatures = [25, 30, 27, 22, 28, 33, 29]
days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
temp_day = list(zip(temperatures, days))
print(temp_day)

# b) Find the maximum temperature from the list and print it along with the corresponding day.
max_temp = max(temperatures)
print("Maximum temperature is: ", max_temp)
for i in temp_day:
    if i[0] == max_temp:
        print("The day of maximum temperature is: ", i[1])

# c) Calculate and print the average temperature.
avg_temp = sum(temperatures)/len(temperatures)
print("Average temperature is: ", avg_temp)


