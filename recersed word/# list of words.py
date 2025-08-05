# list of words 
words = [ 
        'have', 'that', 'they', 'with', 'this', 'from', 'which', 'would', 'will', 
'there', 
        'make', 'when', 'more', 'other', 'what', 'time', 'about', 'than', 'into', 
'could',  
        'state', 'only', 'year', 'some', 'take', 'come', 'these', 'know', 'like', 
'then',  
        'first', 'work', 'such', 'give', 'over', 'think', 'most', 'even', 'find', 
'also',  
        'after', 'many', 'must', 'look', 'before', 'great', 'back', 'through', 
'long',  
        'where', 'much', 'should', 'well', 'people', 'gouda', 'just', 'because', 
'good',  
        'each', 'those', 'feel', 'seem', 'high', 'place', 'little', 'world', 
'very', 'still',  
        'nation', 'hand', 'life', 'tell', 'write', 'become', 'here', 'show', 
'house', 'both',  
        'between', 'need', 'mean', 'call', 'develop', 'under', 'last', 'right', 
'move', 'thing',  
        'general', 'school', 'never', 'same', 'another', 'begin', 'while', 
'number', 'part',  
        'turn', 'real', 'leave', 'might', 'want', 'point', 'form', 'child', 
'small', 'since',  
        'against', 'late', 'home', 'interest', 'large', 'person', 'open', 
'public', 'follow',  
        'during', 'present', 'without', 'again', 'hold', 'codezilla', 'govern', 
'around',  
        'head', 'consider', 'word', 'program', 'problem', 'however', 'lead', 
'system',  
        'order', 'plan', 'keep', 'face', 'group', 'play', 'stand', 'increase',  
        'early', 'course', 'change', 'help', 'line', 'possible', 'fact', 'down' 
        ] 


# genirate a word randomly 
import time
import random

word = words[random.randint(0, len(words) - 1)]

# revers the word 
lst_word = list(word)
lst_word.reverse()
reversed_word  =  "".join(lst_word)


# greet the user and print the reversed  word

print("Welcme to the Reversed Words Game!")
print("-" * 20  ) 
print(f"The Reversed word is: {reversed_word} ")
print("-" * 20  ) 
# get the guess from the user
start_time = time.time()
answer = input("The Word is: ")
end_time = time.time()
print("-" * 20  ) 

# check the answer 
time_taken = end_time - start_time

if answer != word:
    print("Worng Word!")

if time_taken > 10:
    print("You took too long!")

if answer == word and time_taken <= 10:
    print("You Won!")
else:
    print("You Lost!")



https://www.programiz.com/online-compiler/8P7tCAEG8lxZE