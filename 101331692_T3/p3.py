# Intitialize variables
user_Paragraph = ""
uppercase = ""
number_Words = 0
number_Sentences = 0

# Intitialize list
word_List = []
sentence_List = []
new_List = []

# Assign value to variables
user_Paragraph = input("Please write a paragraph and hit enter when you're finished.:\n")

# Assign values to list as elements
word_List = user_Paragraph.split()
sentence_List = user_Paragraph.split('.') # sentences end with '.'

# Assign value to variables
number_Words = len(word_List)
number_Sentences = len(sentence_List)-1 # -1 since '' is counted
index = number_Sentences-1

# For each iteration get the first letter of the first word for 
# every sentence in the list: sentence_List and use the fuction 
# upper to upercase the letter.
# Concatenate the new letter with the rest of the sentence
# Add the new sentence to a new list
for i in range(number_Sentences):
    uppercase = sentence_List[index-i].strip() # Get rid of ' ' before every sentence
    new_List.append(uppercase[0].upper() + uppercase[1:])

# Output
print("\nSample output:", end='\n')
print(f"\nTotal number of words = {number_Words}")
print(f"Total number of sentences = {number_Sentences}", end='\n')
print("\nCapitalized setences are:", end='\n')

# Output every line in the list
for i in range(number_Sentences):
    print(new_List[index-i], end='\n')