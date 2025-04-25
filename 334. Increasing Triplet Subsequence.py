def increasingTriplet(nums):
    first = second = float('inf')
    
    for num in nums:
        if num <= first:
            first = num
        elif num <= second:
            second = num
        else:
            return True
    
    return False
nums = [1, 8, 3, 9, 2]
print(increasingTriplet(nums))