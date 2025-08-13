# words = [ 
#         'each', 'those', 'feel', 'seem', 'high', 'place', 
# 'little', 'world', 'very', 'still',  
#         'nation', 'hand', 'life', 'tell', 'write', 'become', 
# 'here', 'show', 'house', 'both',  
#         'between', 'need', 'mean', 'call', 'develop', 'under', 
# 'last', 'right', 'move', 'thing',  
#         'general', 'school', 'never', 'same', 'another', 
# 'begin', 'while', 'number', 'part',  
#         'turn', 'real', 'leave', 'might', 'want', 'point', 
# 'form', 'child', 'small', 'since',  
#         'against', 'late', 'home', 'interest', 'large', 
# 'person', 'open', 'public', 'follow',  
#         'during', 'present', 'without', 'again', 'hold', 
# 'codezilla', 'govern', 'around',  
#         'head', 'consider', 'word', 'program', 'problem', 
# 'however', 'lead', 'system',  
#         'order', 'plan', 'keep', 'face', 'group', 'play', 
# 'stand', 'increase',  
#         'early', 'course', 'change', 'help', 'line', 
# 'possible', 'fact', 'down'] 

# # get the word from the user
# user_input = input("Enter a word to search for: ").lower()
# result = False
# # check if the word in the list 
# for word in words: 
#     if word.lower() == user_input:
#         result = True
# # print the result
# if result:
#     print(f"the word '{user_input}' was found")
# else:
#     print(f"the word '{user_input}' wasn't found")




# # 2 )

# # get a number from the user
# number = int(input('Enter a number: '))
# # check if the number is a prime num or not 
# if ((number % number == 0 )and (number % 2 != 0 )) or number == 2:
#     print(f"{number} is a Prim number")
# else:    
#     print(f"{number} isn't a Prim number")





# # 3)
# numbers = [-500, -694, -762, -445, -348, -361, -758, -594,  -954, -861, -610, -549, -336, -400, -600, -836, -671, -573,  -555, -390, -450, -811, -849, -870, -815, -694, -951, -588,  -484, -609, -674, -411, -408, -498, -649, -541, -441, -839,  -567, -898]
# postive_numbers = []
# for num in numbers:
#     postive_numbers.append(abs(num))
# print(postive_numbers)    




# lst_words = [['have', 'that', 'they', 'with', 'this', 'from', 
# 'which', 'would', 'will', 'there', 'make', 'when', 'more', 
# 'other', 'what', 'time', 'about', 'than', 'into', 'could'],  
# [ 'state', 'only', 'year', 'some', 'take', 'come', 'these', 
# 'know', 'like', 'then', 'first', 'work', 'such', 'give', 
# 'over', 'think', 'most', 'even', 'find', 'also', 'after', 
# 'many', 'must', 'look', 'before', 'great', 'back', 'through', 
# 'long'],  
# [ 'where', 'much', 'should', 'well', 'people', 'gouda', 'just', 
# 'because', 'good', 'each', 'those', 'feel', 'seem', 'high', 
# 'place', 'little', 'world', 'very', 'still', 'nation', 'hand', 
# 'life', 'tell', 'write', 'become', 'here', 'show', 'house', 
# 'both', 'between', 'need', 'mean', 'call', 'develop', 'under', 
# 'last', 'right', 'move', 'thing'],  
# ['general', 'school', 'never', 'same', 'another', 'begin', 
# 'while', 'number', 'part', 'turn', 'real', 'leave', 'might', 
# 'want', 'point', 'form', 'child', 'small', 'since', 'against', 
# 'late', 'home', 'interest', 'large', 'person', 'open', 
# 'public', 'follow', 'during', 'present', 'without', 'again', 
# 'hold', 'codezilla', 'govern', 'around', 'head', 'consider', 
# 'word', 'program', 'problem', 'however', 'lead', 'system'], 
# ['order', 'plan', 'keep', 'face', 'group', 'play', 'stand', 
# 'increase', 'early', 'course', 'change', 'help', 'line', 
# 'possible', 'fact', 'down']]


# a_counter = 0
# e_counter = 0
# for lst in lst_words:
#     for word in lst:
#         for letter in word:
#             if letter.lower() == "a":
#                 a_counter += 1 
#             elif letter.lower() == "e":
#                 e_counter += 1
# print(f"a: {a_counter}\ne: {e_counter}")                






https://www.programiz.com/online-compiler/7UmGb47iBZzaj