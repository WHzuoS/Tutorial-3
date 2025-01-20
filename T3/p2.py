# Initialize varibles.
food_Items_Mean_Length = 0
index = 0

# Initialize lists.
menu = []
food_Items = []
prices = []
quantities = []
new_Prices = []

# 1

# a.
# Assign values to the lists.
# Order: string, float, integer.
menu = ["Double-Double", 3.40, 8, "Cheeseburger", 2.35, 2, "Hamburger", 2.05,
        1, "Animal Style French Fries", 4.93, 10, "Vanilla Shake", 3.18, 15, 
        "Protein Style Double-Double", 6.60, 3, "Coca-Cola", 1.80, 7]

# 2

# a.
# Creating sublists to categorize main list items.
# Slicing method [start: end: step] used to determine the posiion of 
# string, float, and integer elements.
# Assign the elements with the same data type to the new sublists.
food_Items = menu[0:19:3]
prices = menu[1:20:3]
quantities = menu[2:21:3]

# b.
# Assign values to variables.
# Use the function len() to determine the mean of the sublist: 
# food_Items.
food_Items_Mean_Length = len(food_Items)
index = food_Items_Mean_Length-1

# c. and d.
# The purpose of the for loop is to iterate the block of code
# therefore assign new elements to a list for a set number of times.
# New elements are the products of the two sublists: prices and 
# quatities muiltiplied and rounded two decimal places.
# Replace each element in quantities with associated ASCII 
# uppercase letter individually.
# Index is a reverse counter starting near the end of the sublist 
# index.
for i in range(food_Items_Mean_Length):
    new_Prices.append(round(prices[index] * quantities[index],2))
    quantities[index] = chr(quantities[index] + 64)
    index-=1

# Overwrite index
index = 0

# 3   

# a.
# Output.
# The purpose of for loop is to iterate the output of the sublists 
# with different elements.
print(f"The mean length of the item names is {food_Items_Mean_Length}\n", 
      end='\n')
print("Menu Order Summary: (Food Name: Price, Quantity)\n", end='\n')
for i in range(food_Items_Mean_Length):
    print(f"\t{food_Items[index]}: {new_Prices[index]} , {quantities[index]}\n", end='\n')
    index+=1

