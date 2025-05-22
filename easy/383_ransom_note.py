# Given two strings ransomNote and magazine, 
# return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

def canConstruct(ransomNote, magazine):
    """
    :type ransomNote: str
    :type magazine: str
    :rtype: bool
    """
    magazine_freq = {}
    note_freq = {}
    for c in magazine:
        if c in magazine_freq:
            magazine_freq[c] += 1
        else:
            magazine_freq[c] = 1

    for c in ransomNote:
        if c in note_freq:
            note_freq[c] += 1
        else:
            note_freq[c] = 1
    
    for c in note_freq:
        if c in magazine_freq:
            if note_freq[c] > magazine_freq[c]:
                return False
        else:
            return False

    return True 

#Created a dictinoary to keep track of the count of both strings
#Afterwards compared the 2 counts
        