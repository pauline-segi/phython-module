# lists need a name

# Store multiple data points
# square brackets open and close with nothing in it, means a list

#lists can take multiple data and element types
# the elements are separated by a comma in the list
# for example, the following incldes: str, int, float, list
# list_name = ["Asli",1,4.5,[]] 

# it makes sense to store similar elements in a group (like numbers etc)

# this list has five elements in it:
# digits = [1,2,3,4,5] 
# list elements always start from zero, and they are 'indexed' base, so the one above has only 4 indexes, as the first is zero
# Lists are indexed based which start from zero 0



# if you're getting an error, it will show you which line is erroring and this is the error code you'll get: IndexError: list index out of range --- and the code won't work after this line --- for example like the following: 
# print(digits[5]) IndexError: list index out of range

# if you want to find the very last element in a list, you can use -1 to show the very last element

# Slicing: if you want to get specific elements in a list, for example in our list we want the first three elements, we need to specify the starting index, followed by a colon: and an ending index of where you want to stop extracting the data (the ending index will not be shown, it will show you the element directly before it) 
# Start (inclusive) and End (inclusive)
# If you don't put a closing value after the starting value and colon, it will show you everything in the list
# if you want to get the final number, you need to specify one greater than what the list has (so in this case, we say 5 as there's only 4)
# if you add a second colon, and put a 1 (0:5:1) it's saying grab every single digit, if you have (0:5:2) it's saying print every second element, if we do (0:5:3), it's saying skip every third number

# the 'len' function shows you how many elements are in a list

# the dot after the list name is a method (or a function in a way)
# the append function will add an element to the list
# the pop function will remove the index which you have specified, and if nothing is specified, it will remove the last element as default
# nested lists are lists within a list


# digits = [1,2,3,4,5] 
# print(digits[2])
# print(digits[-3])
# print(digits[0:4])
# print(digits[-2:5])
# print(digits[0:5:1])
# print(len(digits))
# print(digits)
# digits.append(6)
# print(digits)
# digits.pop(0)
# print(digits)
# digits[1] = 90
# print(digits)
# popped_elements = digits.pop(0)
# print(popped_elements)

letters = ['a','b','c','d',['Emily','Julie']]
print(letters[4][0]) #This gets the 4th element from the first list, and then the 0 (first) element from the second list

if 'Emily' in letters:
    print("It is in the list") #this is a search function to be able to find if there is the element in the list