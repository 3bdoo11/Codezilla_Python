def max_even_number(*nums, nth_max_even_number=0):
    nums_list = []
    for num in nums:
        if num % 2 ==0:
            nums_list.append(num)
            
        nums_list.sort(reverse =True)
    
    if nth_max_even_number:
        nth_max = nums_list[nth_max_even_number-1]
        
        return nth_max
    else:    
        return max(nums_list)
        
        
max_even = max_even_number(64, 52, 84, 76, 45, 36, 88)  

third_max_even = max_even_number(64, 52, 84, 76, 45, 36, 88, nth_max_even_number=3)


print(f"Max even number: {max_even}")
print(f"Third max even number : {third_max_even}")