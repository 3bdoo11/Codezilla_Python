numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
neg_numbers = [-1, -2, -3, -4, -5, -6, -7, -8, -9]
def minimum_odd_number(numbers):
    minimum = []
    for num in numbers:
        if num % 2 != 0:
            minimum.append(num)
    #minimum.sort()
    return min(minimum)
print(minimum_odd_number(numbers))        

            
def minimum_negative_odd_number(neg_numbers):
    minimum = -1
    for num in neg_numbers:
        if num % 2 != 0:
            if num < minimum:
                minimum = num
    return minimum
        
print(minimum_negative_odd_number(neg_numbers))