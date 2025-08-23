nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13]
def sum_nums(nums ,only_even=False, only_odd=False, only_positive =False, only_neg=False):
    total =0
    for num in nums:
        if only_even:
            if num % 2 ==0:
                total += num
        elif only_odd:
            if num % 2!=0:
                total += num
        elif only_positive:
            if num > 0:
                total += num
        elif only_neg:
            if num < 0:
                total += num
        else:
            total += num
    return total        

result = sum_nums(nums) 
print(result)
        
