# while True:
#     user_input = input("> ")
#     if user_input.startswith("#") or len(user_input) == 0:
#         continue
#     if user_input.lower() == "done":
#         print("Done!")
#         break
#     print(user_input)





# # import the moudules
# import random

# # generate a number between 1 , 100

# number = random.randint(1, 100)
# print(number)
# attempts = 0

# while True:
#     attempts += 1
#     guess = int(input("Guess the number: "))
#     if number == guess:
#         if attempts == 1:
#             print("Amazing, you gessed the number from the first try !")
#         else:    
#             print(f"You gessed the number in {attempts} attemps")
#         break
#     elif number > guess:
#         print("Too low, try again")
#     elif number < guess:
#         print("Too high, try again")






# # find the first multiple of 7 in a list of numbers 
# numbers = [953, 776, 532, 665, 973, 683, 484, 499, 741, 980]

# attempts = 0

# while len(numbers) > attempts:
#     if numbers[attempts] % 7 == 0:
#         print(f"{numbers[attempts]} multiple of 7")
#         break
#     attempts += 1    






# all_scores = []

# while True:
#     score = input("Enter a score (or type a 'done' ot exit): ")
#     if score.lower() == "done" or len(score) == 0:
#         break
#     all_scores.append(float(score))
    
# avrage = sum(all_scores) / len(all_scores)    

# print(f"The average of the score is: {avrage:.2f}")







https://www.programiz.com/online-compiler/6Hd9kwJv0L6cj