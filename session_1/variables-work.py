# Create a variable named first_name and assign Pauline to it
first_name = "Pauline"
last_name = "Segi"
programming_language = "Python"

# Data Types - Text data and Numerical data
# Text data - String (and you always need to put "quotes" between the piece of data your use)
# The standard convention for Python language is to always name using lowercase
# Functions are aiming to do a specific task (so print, means it's aiming to print whatever you have put there to the screen)
# the 'print' function is a great way to troubleshoot an error in your code, so it's great to print as you go to see what you're doing to that variable
# the f in the print section stands for 'format'

today = "Tuesday"
# print(today)
# print(f"Today is {today}")
# print(type(today))


# Numerical data types - Integer and Float
# Integer means a Number, but it means a whole number
# when using numerical data types, you don't need to use "quotes"
# So in those curly brackets, you can calculate things too -- you can manipulate the data

parkers_age = 4
# print(type(parkers_age))
# print(f"Parker is turning {parkers_age+1} soon!")

height = 174
# print(f"My height is {height/100} in m.")

# This is an example of Float, its not a whole number

weight = 74.7
# print(f"My weight is {weight*2.1} in lbs")

distance = "5000"
# print(int(distance) + 8)
# print(distance + str(8))


# The input function is saying hey we need to store something, and you name it as a variable

# print("Hello")
# dog_name = input("What is your dog's name?")
# print(f"Nice to meet you {dog_name}")

# whenever you make use of the input function, it stores the data as string, always

birth_year = input("What year were you born?")
print(f"You are {2023-int(birth_year)} years old.")

