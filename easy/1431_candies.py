# There are n kids with candies. You are given an integer array candies, 
# where each candies[i] represents the number of candies the ith kid has, 
# and an integer extraCandies, denoting the number of extra candies that you have.

# Return a boolean array result of length n, where result[i] is true if, 
# after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, 
# or false otherwise.

# Note that multiple kids can have the greatest number of candies.


def kidsWithCandies(candies, extraCandies):
    greatest_amount = []
    greatest_among_kids = candies[0]
    for kid in candies:
        if kid > greatest_among_kids:
            greatest_among_kids = kid
    
    for i in range(len(candies)):
        candies[i] += extraCandies
        if candies[i] >= greatest_among_kids:
            greatest_amount.append(True)
        else:
            greatest_amount.append(False)

    return greatest_amount


# First the kid with the largest amount of candies needs to be found and that is the standard
# Then going through each kid add the extra candies, and determine if they now have more or equal to the kid with most number of candies
    