# For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t 
# (i.e., t is concatenated with itself one or more times).

# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.


class Solution(object):
    def gcdOfStrings(self, str1, str2):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        if str1 + str2 == str2 + str1:
            gcd_length = gcd(len(str1), len(str2))
            return str1[:gcd_length]
        else:
            return ""
        

# The greatest common diviser of a number would be find the product of a and b. That would then be divided by the LCM of both number
# The function loops a, b = b, a % b until b is 0, which it then returns a
# The Solution then returns the gcd length of the string
                

        