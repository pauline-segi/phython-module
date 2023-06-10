# Function - an activity that is natural to or the prupose or a person or thing.
# Functions we've already seen
# input(), len(), int(). print() # Every function has a bracket, and it only performs a specific task (input always asks the user for an input, len always gives you the length)



# Task Seperation



# Function definition

# use def to define a function and they must always have brackets.

# Calling a function

# you need a def to create a function, and then you need to call it, which is using the 'name of the function' --- the function definition always needs to come before, and then you can call it

#So below, as you print the function, it goes through line 20, and runs the function, then it skips line 21 as you haven't called it, and then goes to line 23 as you've called it

# def ask_user_name(): #here you create a function
#     print("Now function is entered")
#     name = input("What is your name: ")
# print("Hello")
# ask_user_name() #here you are calling a function
# print("Hi")


# def ask_user_name():
#     name = input("What is your name: ")
#     print(name) #print does not mean 'return' and we want it to return
#     return name #anything after return in this particular function will not print -- return ends the function, so if we try print after it, nothing will print out




# def ask_user_age():
#     age = input("How old are you: ")
#     if age >= 18:
#         print("Welcome")
#     else:
#         print("You cannot enter.")

# Any fucntion that doesn't return anything will automatically return an instance of the None datatype


# Parameters

def add(number1, number2): # so for only the body of the function, these parameters are created (number1 and number2), so number1 and number2 are known as the parameters, these get used as variables in our code block, they dont' have values yet, as we're just defining the function
    result = number1 + number2 #the result variable, is now completing the function of the parameters
    return result 
#if you ever create a variable inside of a function, it's called a 'local variable' and exists only in the function, it does not exist outside the function --- but if you create a variable outside a fucntion (like the normal variables we've made) it exists 'globally' (in or out of a function) and is a 'global variable'

#now we want to call the function with two arguments, so it will start at line 53, then use the call below to give a value to the variables in the def above (so now, number1 = value 2, and number2 = the value of 3)
answer = add(2,3) #when you're calling a function with a value there, it's called an 'actual parameter'
print(answer)

