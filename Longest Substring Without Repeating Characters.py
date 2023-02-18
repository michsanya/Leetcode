"""
Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        char_set = set()
        for i, char in enumerate(s):
            max_len_new = 0
            char_set = set()
            for letter in s[i:]:
                if letter not in char_set:
                    char_set.add(letter)
                    max_len_new = len(char_set)
                else:
                    break
            max_len = max(max_len, max_len_new)
        return max_len

s = Solution()
res = s.lengthOfLongestSubstring('abcabcbb')
print(res)