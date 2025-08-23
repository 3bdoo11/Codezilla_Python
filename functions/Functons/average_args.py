def average(*args):
    if len(args) == 1 and isinstance(args[0], (list, tuple, set)):
        args = args[0]
    return sum(args) / len(args)

average1 = average(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
average2 = average([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])    
average3 = average((1, 2, 3, 4, 5, 6, 7, 8, 9, 10))   
average4 = average({1, 2, 3, 4, 5, 6, 7, 8, 9, 10})    


print(f"Average1: {average1}")
print(f"Average2: {average2}")
print(f"Average3: {average3}")
print(f"Average4: {average4}")
