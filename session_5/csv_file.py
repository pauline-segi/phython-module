# When writing this, you can follow the pattern which pops up by the program automatically
# you'll do the file first, and then "r" stands for Reading -- the "r" is the default
# Generally, by default, the coding is always "utf-8", the "utf-8" is the default
# So:
# open("dogs_are_awesome.csv","r","utf-8",)
# open("dogs_are_awesome.csv")
# The two lines above are exactly the same, as the "r" and "utf-8" are defaults
# Syntax, you want 'with', then 'open' followed by the file you want to open
# (if i ever come across it, module means just another python file)

import csv

# with open(file="dogs_are_awesome.csv",mode="r",encoding="utf-8") as my_file:
#     csv_reader = csv.reader(my_file)
#     for row in csv_reader:
#         print(row)


with open(file="hello.csv",mode="w") as my_file:
    csv_writer = csv.writer(my_file)
    csv_writer.writerow("Hello")
    