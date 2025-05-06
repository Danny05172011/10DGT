#Demonstrate how variables are created and how they work
#Author: Danny Kim
#Date: 11 April 2025
#Version 1.0

#Different types of variables
#Store a number 
My_number= 80 # assigning 80 to my_number (variable)
Print(My_number)

My_number2= 7 # I have reassigned the value of the variable
print(My_number2)

# Store a string 
name_1 = "Danny"
print(name_1)

# Assign the value of one variable to another
My_number = name_1
print(My_number) # Don't assign values to variables that don't make sense

# Creating a bew variable
num_1 = 5 
num_2 = 17

'''Do calculations with variables and store the result in 
# another variable. I can now
press ter
as
many times 
 as I want'''

sum = 5 + 7 # This is not good practice
print(sum)

# better way
sum1 = num_1 + num_2 
print(sum1)

sum_string1 = "17" # This stores a string 
sum_string2 = "5"

#Adding strings togetther is called concatenation.
sum = sum_string2 + sum_string1 
print(sum)
print(sum1)

print(f"My calculation for {sum_string1} + {sum_string2} = {sum}")


