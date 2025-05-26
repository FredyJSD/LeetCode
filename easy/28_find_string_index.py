# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, 
# or -1 if needle is not part of haystack.

#Solution
def strStr(haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1

#If needle is in haystack it returns the index it starts at
#Otherwise return -1
