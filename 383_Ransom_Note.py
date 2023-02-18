class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for letter in ransomNote:
            len_before = len(magazine)
            magazine = magazine.replace(letter, '', 1)
            len_after = len(magazine)
            if len_before == len_after:
                return False
        return True

print(Solution().canConstruct('qwe','qwer'))
