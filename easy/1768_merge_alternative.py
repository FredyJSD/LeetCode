# You are given two strings word1 and word2. 
# Merge the strings by adding letters in alternating order, starting with word1. 
# If a string is longer than the other, append the additional letters onto the end of the merged string.


def mergeAlternately(word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: str
    """
    longer_word = len(word1) if len(word1) > len(word2) else len(word2)
    word = []
    for i in range(longer_word):
        if i < len(word1):
            word.append(word1[i])
        if i < len(word2):
            word.append(word2[i])

    return ''.join(word)       


# Check which word is longer that way when the shorter word is complete it keeps adding the extra letters of the long word
# Make sure to check if a char is in that position and add it
# Use .join() to turn the array into a string

    