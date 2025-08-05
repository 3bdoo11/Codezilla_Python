print("It is the time to see if we could do better 😀")
print("-"*20)

Num = float(input("Enter the Num: "))
Num_divide = float(input("Enter the Num to divide by: "))
answer = input(f"{Num} is divisible by {Num_divide} yes or no? 🤔🤔\n").lower().strip()
Divide = Num % Num_divide

if Divide == 0:
    Correct = "yes"
else:
    Correct = "no"

if answer == Correct:
    print("Bravoooo!!🥳🥳🥳")
else:
    print("No problem, let's try again 😀")




https://www.programiz.com/online-compiler/865FcGSqJoXC4