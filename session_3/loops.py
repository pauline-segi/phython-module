# letters = ['a','b','c']
# This is one way to do a loop
# print(letters[0]) 
# print(letters[1])
# print(letters[2])

# But there is an easier way
# Loops help us to perform a task multiple times

# There are 2 types of loops: while loops, and for loops


# While loops

# So you write 'while' and it creates a condition, almost like an if statement -- so in the following, the 5 > 1 will get executed if the condition is True --- the following creates an infinite loop, so it never ends --- so it's very important with while conditions to make the statement false, so there's something to exit the loop
# while 5 > 1:
#     print("Hello")

# So to exit the infinite loop, we change the code to add a count in, so it only counts to a certain number --- in this case, we have it as count + 1, so it will only count until the 5, as 5 is not greater than 5:
# count = 0
# while 5 > count:
#     print("Hello")
#     count = count + 1

# you can also write 'count + 1' as 'count += 1'

# This is using loops by using strings, you want to cancel the loop by putting in a question via the input section so if the wrong name is put in, the loop (I dont know you) won't just keep running
# name = input("What is your name? ")
# while name != "Ashley":
#     print("I don't know you!")
#     name = input("Well, what's the new name?")


# If you want to change a users input to a number, you can use the function 'f' with the curly brackets to make it a number which you can add to the users input, like th efollowing
# enter = input("Enter a number: ")
# count = 0 #need to check input is blank
# while enter != "":
#     count += int(enter)
#     enter = input("Enter a number: ")
# print(f"Your numbers sum to {count}")



# for loops


#so the letter is a variable name, and that variable name actually gets assigned to each of the string characters in the list. so the first time it goes into this loop, it knows to start in the list and go to the end -- so this will print letter a --- once that loop is finished, it goes back changes the letter assigned variable and goes back to b ------- also, the variable (in this case, 'letter') can be absolutely anything, it doesnt have to be a specific thing --- 
# letters = ['a','b','c']
# for letter in letters:  
#     print(letter)


# in the following, we're not going through a list, you're just asking it to print the range ten times (very similar to slicing in lists, where you could have 'number[0:10]' so it'll count from zero and count until the 10th element (which is 9))
# so you can use this for function if you want to count something, it's handy for other things to --- 
# for number in range(10):
#     print(number)


students = [
    ["Cindy","Emily","Eve"],
    ["Julie","Maddy","Andrea"],
    ["Jenny","Sarah","Yara"]
    ]

# so what this code is doing, it's say go into my students list, and get all the elements from the list (so thats how it gets the first line), then go in again and get each element individually in that list and print that (that's how you get each name individually in the list):
for student in students:
    print(student)
    for name in student:
        print(name)
