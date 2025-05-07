# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# 1. Open brackets must be closed by the same type of brackets.
# 2. Open brackets must be closed in the correct order.
# 3. Every close bracket has a corresponding open bracket of the same type.


#Attempt 1
class Solution(object):
    def isValid(self, s):
        foundPairs = False
        for i in range(len(s)):
            if s[i] == "(":
                for j in range(i+1, len(s)):
                    if s[j] != ")":
                        foundPairs = True
            elif s[i] == "[":
                for j in range(i+1, len(s)):
                    if s[j] == "]":
                        foundPairs = True
            elif s[i] == "{":
                for j in range(i+1, len(s)):
                    if s[j] == "}":
                        foundPairs = True
        return foundPairs


# It doesnt enforce order of nesting
# multiple openings and closings of same type isnt tracked


#Attempt 2
#Using stack
class Solution(object):
    def isValid(self, s):
        stack = []
        for i in range(len(s)):
            if s[i] == "(" or s[i] == "[" or s[i] == "{":
                stack.append(s[i])
            elif s[i] == ")":
                if stack[-1] == "(":
                    stack.pop()
            elif s[i] == "}":
                if stack[-1]== "{":
                    stack.pop()
            elif s[i] == "]":
                if stack[-1]== "[":
                    stack.pop()
        return not stack


#Final Solution
class Solution(object):
    def isValid(self, s):
        stack = []
        for i in range(len(s)):
            if s[i] == "(" or s[i] == "[" or s[i] == "{":
                stack.append(s[i])
            elif s[i] == ")":
                if not stack or stack[-1] != "(":
                    return False
                stack.pop()
            elif s[i] == "}":
                if not stack or stack[-1] != "{":
                    return False
                stack.pop()
            elif s[i] == "]":
                if not stack or stack[-1] != "[":
                    return False
                stack.pop()
        return not stack


# Notes:
# To check is stack is empty (not stack)
# stack.pop() removes the last item added
# To peek the last item added or last item in list (stack[-1])

Sol = Solution()
s = "()[]{}"
print(Sol.isValid(s))
t = "([])"
print(Sol.isValid(t))
