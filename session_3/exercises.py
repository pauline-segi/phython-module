# enter = input("Enter a number: ")
# count = 0 #need to check input is blank
# while enter != "":
#     count += int(enter)
#     enter = input("Enter a number: ")
# print(f"Your numbers sum to {count}")


# Another way to do this is:

# number = input("Enter a number: ")
# sum = 0
# while number:
#     sum = sum + int(number)
#     number = input("Enter another number: ")
# print(sum)


# loop 2:


# number = input("Enter a number: ")
# list_of_numbers = range(int(number)+1)
# odd_numbers_list = []
# for number in list_of_numbers:
#     if number % 2 == 0:
#         pass
#     else:
#         odd_numbers_list.append(number)
# print(odd_numbers_list)

# don't do it this way, as it's not good to do it all on one line -- no one else can read your code:
# number = int(input("Number please:"))
# print([number for number in list(range(1, number+1, 2))])

