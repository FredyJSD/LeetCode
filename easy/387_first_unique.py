# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

#Solution
def firstUniqChar(s):
        """
        :type s: str
        :rtype: int
        """
        non_repeat = {}
        for c in s:
            if c in non_repeat:
                non_repeat[c] += 1
            else:
                non_repeat[c] = 1
        
        index = float('inf')
        for c in non_repeat:
            if non_repeat[c] == 1:
                if s.index(c) < index:
                    index = s.index(c)

        if index == float('inf'):
            return -1
        else:
            return index

#Keep track of total number each character appears
#Find the index that the character is at

