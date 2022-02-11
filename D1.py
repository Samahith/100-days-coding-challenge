# 100 Days coding challenge
# basic to advance
# day 1

# exercise 1
#  debugging excersise
# read me
"""
Required output:
Day 1 String-Manuplation
string concatination is done by adding + sign to two or more strings or variables
Example:
print("hello!" + "world")
new lines can be created by adding a backslash and "n"

" debug the below code "
 """
print("Day 1 String-Manuplation")
print("string concatination is done by adding + sign to two or more strings or variables")
print("Example: \n print(\'hello!' + \'world')")
print("new lines can be created by adding a backslash and \'n'")


#  excercise  2  (input function)
# Readme
"""
 write a program which calculate's the number of charecters present in their user name
"""
# # code

name = input("Please enter your username \n >>> ")
name_length = len(name)
print(f"your username  has {name_length} charecters")

# exercise 3 (varibles in python)
# READme
"""
write a program where the stored input's can be interchanged
"""
a = input("please enter anything \n >>> ")
b = input("please enter anything for your second variable \n >>> ")
c = a
a = b
b = c

print ( a , b)

# project 1

#  create a simple brand name generator
place = input("Please enter your hometown name \n >>> ")
pets_name = input("Please enter your pet's name \n >>> ")
band_name = f"{place} {pets_name}"
print(f"your band name is {band_name}")
