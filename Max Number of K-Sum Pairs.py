from collections import Counter

def maxOperations(nums, k):
    count = Counter(nums)
    operations = 0
    
    for num in count:
        complement = k - num
        if num == complement:
            # If num == complement, we can only pair the same numbers
            operations += count[num] // 2
        elif num < complement:  # Ensure each pair is only counted once
            # We can pair 'num' and 'complement' as many times as both exist
            operations += min(count[num], count[complement])
    
    return operations
nums = [1, 2,3,4]
k = 5


print(maxOperations(nums,k))
