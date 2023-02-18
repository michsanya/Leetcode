class Solution:
    def longestPalindrome(self, s: str) -> str:
        """    TODO: 02.10.22
        length = len(s)
        if length < 2:
            return s
        longest_palindrome = []
        for i in range(len(s) - 2):
            if s[i] == s[i + 1]:
                longest_palindrome = [s[i]]

        return ''.join(longest_palindrome)
        """




s = Solution()
ans = s.longestPalindrome('vbghghgh')
print(ans)
