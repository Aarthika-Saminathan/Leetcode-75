def maximum_candies(candies, extracandies):
    result = []
    max_candy = max(candies)
    for candy in candies:
        if candy + extracandies >= max_candy:
            result.append(True)
        else:
            result.append(False)
    return result
           
candies = [2, 3, 5, 1, 3]
extraCandies = 3
print(maximum_candies(candies, extraCandies))  # Output: [True, True, True, False, True]
