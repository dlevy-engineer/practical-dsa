"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.


Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true


Constraints:
1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
"""

def canConstruct(ransomNote: str,
                 magazine: str) -> bool:
    
    c_dic = {}
    
    for c in magazine:
        c_dic[c] = c_dic.get(c, 0) + 1

    for c in ransomNote:
        if c not in c_dic:
            return False
        
        elif c_dic[c] == 1:
            del c_dic[c]

        else:
            c_dic[c] -= 1
    
    return True


from collections import Counter

def canConstructWithCounter(ransomNote: str,
                            magazine: str) -> bool:
    
    rn = Counter(ransomNote)
    m = Counter(magazine)

    for c in rn:
        if rn[c] > m[c]:
            return False
    
    return True