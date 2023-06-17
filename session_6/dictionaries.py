# Lists
# numbers = [1,2,3]
# numbers[0]
# Dictionary
# Dictionaries can hold a value of dictionaries, lists etc.

#dictionaries stores key and value pairs --- this is dictionary with one element, key is the left side, the right hand side is the value, so if you were to get the value of this element, you refer to the key, and elements are separated by the comma
#Dicionary keys are unique -- like in a dictionary, the word is only in there once

#Values can be any data type

#Keys can only be immutable data types (immutable means it can't be changed - they are usually the single units like strings, integers, floats, buleans ---  mutable means they can change, like lists where you apend or pop them)

# student_phonebook = {
#     "Cindy":111,
#     "Tracey":123,
#     "Pauline":444
# } 

# print(student_phonebook)
# # print(type(student_phonebook)) #this tells you the type
# student_phonebook["Yara"] = 555 #this line will add Yara to the Dictionary, so the Key is in brackets but the value is out
# print(student_phonebook)


#let's see what happens wehn the key does not exisit in the dictionary

# print(student_phonebook)
# student_phonebook["Asli"]
# print(student_phonebook)


#here you can cahnge the value of an element in the list
# print(student_phonebook)
# student_phonebook["Cindy"] = 555
# print(student_phonebook)


#this is deleting a key and value from a list, you use the del function
# print(student_phonebook)
# del student_phonebook["Tracey"]
# print(student_phonebook)



student_phonebook = {
    "Cindy":111,
    "Tracey":123,
    "Pauline":444
} 


#what if you want to extract the keys and values rather than being in a list
#so if you loop gthrough a dictionary, as  default, it gives you the keys

# for element in student_phonebook:
#     print(element)



#if I want to grab a value, pass in the key in square brackets and basically telling it to give me the value

# for key in student_phonebook:
#     print(key, student_phonebook[key])



#there's another method called values, it's iterating through all the values -- and will print only the values not the keys

# for value in student_phonebook.values():
#     print(value)


#this is called unpacking, so in this list we can print the values and 'unpack' them from the list
a,b = [1,2]
# print(a)
# print(b)


# **** the number of variables when unpacking a list, need to always match the number of elements in a list ****


#another method is items, so this actually goes through each element which is a key and value pair, and gives you a tuple -- tuple is basically a data type that can hold mroe than one value separated by comma -- this is unpacking

# for example in student_phonebook.items():
#     print(example)


#this is doing the same thing, but in a different way, and it also only grabs the elements with no brackets
# for key,value in student_phonebook.items():
#     print(key,value)


