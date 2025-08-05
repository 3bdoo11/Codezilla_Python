# txt = """One of the most effective ways to reduce the friction 
# associated with 
# your habits is to practice environment design 
# In a previous chapter we discussed environment design as a 
# method for making cues more 
# obvious but you can also optimize your environment to make 
# actions 
# easier 
# For example when deciding where to practice a new habit it is 
# best to choose a place that is already along the path of your 
# daily 
# routine 
# Habits are easier to build when they fit into the flow of your 
# life  
# You are more likely to go to the gym if it is on your way to 
# work 
# because stopping does not add much friction to your lifestyle 
# """

# letter_counter = {}
# for letter in txt.lower():
#     if letter not in [" ", "\n"]:
#         if letter not in letter_counter:
#             letter_counter[letter] = 1
#         else:
#             letter_counter[letter] += 1
# for letter, count in letter_counter.items():
#     print(f"{letter.capitalize()}: {count}")


# txt = """One of the most effective ways to reduce the friction 
# associated with 
# your habits is to practice environment design 
# In a previous chapter we discussed environment design as a 
# method for making cues more 
# obvious but you can also optimize your environment to make 
# actions 
# easier 
# For example when deciding where to practice a new habit it is 
# best to choose a place that is already along the path of your 
# daily 
# routine 
# Habits are easier to build when they fit into the flow of your 
# life  
# You are more likely to go to the gym if it is on your way to 
# work 
# because stopping does not add much friction to your lifestyle 
# """

# letter_counter = {}
# for letter in txt.lower():
#     if letter not in [" ", "\n"]:
#         letter_counter[letter] = letter_counter.get(letter, 0) +1
# for letter, count in letter_counter.items():
#     print(f"{letter.capitalize()}: {count}")
      




# txt = """One of the most effective ways to reduce the friction 
# associated with 
# your habits is to practice environment design 
# In a previous chapter we discussed environment design as a 
# method for making cues more 
# obvious but you can also optimize your environment to make 
# actions 
# easier 
# For example when deciding where to practice a new habit it is 
# best to choose a place that is already along the path of your 
# daily 
# routine 
# Habits are easier to build when they fit into the flow of your 
# life  
# You are more likely to go to the gym if it is on your way to 
# work 
# because stopping does not add much friction to your lifestyle 
# """ 

# letter_counter = {}
# for letter in txt.lower():
#     if letter not in [" ", "\n"]:
#         letter_counter[letter] = letter_counter.setdefault(letter, 0) +1
# for letter, count in letter_counter.items():
#     print(f"{letter.capitalize()}: {count}")
    






# txt = """One of the most effective ways to reduce the friction 
# associated with 
# your habits is to practice environment design 
# In a previous chapter we discussed environment design as a 
# method for making cues more 
# obvious but you can also optimize your environment to make 
# actions 
# easier 
# For example when deciding where to practice a new habit it is 
# best to choose a place that is already along the path of your 
# daily 
# routine 
# Habits are easier to build when they fit into the flow of your 
# life  
# You are more likely to go to the gym if it is on your way to 
# work 
# because stopping does not add much friction to your lifestyle 
# """ 


# word_counter = {}
# lst_txt= txt.lower().split()
# for word in lst_txt:
#     if word not in word_counter:
#         word_counter[word] = 1
#     else:
#         word_counter[word] += 1
# for word, count in word_counter.items():
#     print(f"{word.capitalize()}: {count}")
        


# word_counter = {}
# lst_txt= txt.lower().split()
# for word in lst_txt:
#     word_counter[word] = word_counter.get(word ,0) + 1
# for word, count in word_counter.items():
#     print(f"{word.capitalize()}: {count}")


# word_counter = {}
# lst_txt= txt.lower().split()
# for word in lst_txt:
#     word_counter[word] = word_counter.setdefault(word ,0) + 1
# for word, count in word_counter.items():
#     print(f"{word.capitalize()}: {count}")
       





# february_shopping_list = { 
#     1: ['meat', 'chicken', 'chicken',  
#                       'chicken', 'bread', 'chocolate', 'meat'],  
#     2: ['bread', 'milks', 'butter', 'butter', 'chocolate'],  
#     3: ['butter', 'meat', 'milks'],  
#     4: ['butter', 'bread', 'nuts'],  
#     5: ['butter', 'bread', 'chocolate', 'chocolate'],  
#     6: ['nuts', 'butter', 'butter',  
#                   'butter', 'chocolate', 'butter'],  
#     7: ['cheese', 'milks', 'butter', 'nuts'],  
#     8: ['cheese', 'meat', 'nuts', 'yoghurt', 'cheese'],  
#     9: ['chocolate', 'milks', 'milks',  
#                     'chocolate', 'milks', 'eggs', 'meat'],  
#     10: ['yoghurt', 'butter', 'chocolate', 'cheese', 'butter'],  
#     11: ['cheese', 'meat', 'yoghurt'],  
#     12: ['eggs', 'chocolate', 'meat', 'eggs', 'butter'],  
#     13: ['bread', 'eggs', 'yoghurt',  
#                       'yoghurt', 'chicken', 'chocolate'],  
#     14: ['milks', 'meat', 'meat'],  
#     15: ['meat', 'chicken', 'butter', 'nuts', 'nuts'],  
#     16: ['meat', 'meat', 'chicken'] 
#     } 
    
# items_prices = { 
# 'meat': 250, 
# 'chicken': 140, 
# 'bread': 10, 
# 'chocolate': 20, 
# 'milks': 42, 
# 'butter': 75, 
# 'nuts': 90, 
# 'cheese': 65, 
# 'yoghurt': 25, 
# 'eggs': 120 
# } 

  
# counter = {}

# for day in february_shopping_list.values():
#     for item in day:
#         if item not in counter:
#             counter[item] = {"quantity": 1}
#         else:
#             counter[item]["quantity"] += 1
        
# for grocery in counter:
#     print(f"{grocery.title()}: {counter[grocery]["quantity"]}")
   
   
   
# final = 0
# for item in items_prices:
#     counter[item].update({"price": items_prices[item]})
# print("-"*20)     
# for shoping in counter:
#     price = counter[shoping]["price"]
#     quantity = counter[shoping]["quantity"] 
#     total = price * quantity
#     final +=total
#     print(f"{shoping}: {quantity} X {price}EGP = {total}EGP")
#     print("-"*20) 
# print("-" * 35 )
# print(f"Total items price: {final}EGP")
 
