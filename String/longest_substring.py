# Given a string s, find the length of the longest substring without repeating characters.
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Technique used: Sliding window

def lengthOfLongestSubstring(s: str) -> int:
    #Keeps track of all the characters in our window
    charSet = set()
    #Since we are using sliding window technique we will need two pointers to keep track of the window
    left = 0
    result = 0

    #Right pointer will continuously increase as we check the whole string
    for right in range(len(s)):
        #If we encounter a duplicate character. we have to update our set and window
        while s[right] in charSet: 
            charSet.remove(s[left])
            left +=1 
        
        charSet.add(s[right])
        result = max(result, right-left+1)

    return result