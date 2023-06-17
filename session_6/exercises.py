# Q1.

# groceries = {
#     "Baby Spinach": 2.78,
#     "Hot Chocolate": 3.70,
#     "Crackers": 2.10,
#     "Coffee": 9.00,
#     "Carrots": 0.56,
#     "Oranges": 3.08
# }

# add_list = []

# for key,value in groceries.items():
#     quantity = int(input(f"How many of {key} do you want: "))
#     total_cost = quantity * value
#     add_list.append(total_cost)
# print(f"Total cost: {sum(add_list)}")


# Q2.

import csv
colours_865 = "PlusCSVExamples/colours_865.csv"

with open(colours_865, "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    # for row in csv_reader:
        # print(row)

colour_counts = {
    "blue": 0,
    "green": 0,
    "yellow": 0,
    "red": 0,
    "purple": 0,
    "orange": 0,
}

for rgb,hex,color in colours_865.items():
    print(colours_865)