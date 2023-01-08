# Find the longet substring that we can create with k replacement
# https://leetcode.com/problems/longest-repeating-character-replacement/
# Replace characters that are less frequent
# Technique: Sliding window technique

def characterReplacement(s: str, k: int) -> int:
    #A Hahmap to count the occurances of each character in the string
    count = {}
    #The longet substring that we can create with k replacement
    result = 0

    #Since we are following the sliding window technique, we will need two pointers -> left and right
    left = 0
    for right in range(len(s)):
        # for the character at position right, we increament the count of it
        count[s[right]] = 1 + count.get(s[right], 0)

        #is the current window valid
        while (right-left+1) - max(count.values()) > k:
            count[s[left]] -= 1
            left +=1

        result = max(result, right-left+1)

    return result
