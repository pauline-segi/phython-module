# Boolean

name = "Pauline"
age = 19






# Boolean Expressions - Expressions that produce a boolean value in return 
# Comparison Operators

# print(5 > 3)

# True and False must always be in Capitals to make it a variable

# == is equal to
# != is not equal to
# > greater than
# < less than
# >= greater or equal to
# <= less than or equal to
# 

# print(5 > 3)
# print(3.5 > 6.3)
# print("Pauline" = "pauline")




# Mathematical Operators - Addition, Division, Subtraction, Multiplication





# Boolean Operators - not, and, or

    # not makes the expression reverse
    # and we use between two expressions, so we're combining two boolean expressions and making them one
    # or is asking to check that if the first part or the second part is True, so at least one of those things are True

is_sunny = True
is_warm = True

# print(not is_sunny)
# print(is_sunny or is_warm)

# conditionals check the expression, so if it holds true, the steps that we want are programmed to be true

# In the below, the expression comes from after the 'if' so if is cehcking whether the temp is greater than 18, then it's followed by colon: so after a colon, it puts a space after a colon, so that it goes indented

# syntax means grammar error (like if variable etc) / semantics means the logic of it

# indents are very important

# elif is for else if (it's combined both else and if)
# if there's multiple if's it will check every line regardless if it's true, but if there is one if and then elif's, it will only check the one if and if that's true, it will ignore the elif -- but it will check all if's even if they are true, else captures every other condition

temperature = 20

if temperature <= 18:
    print("Weather is too cold!")
elif temperature > 28:
    print("Weather is too hot!")
else:
    print("Weather is nice!")


    

