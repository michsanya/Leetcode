from unittest import TestCase
from Palindrome_Linked_List import *


class TestSolution(TestCase):

    def test_is_palindrome_1(self):
        solution = Solution()
        ts = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
        self.assertTrue(solution.isPalindrome(ts))

    def test_is_palindrome_2(self):
        solution = Solution()
        self.assertTrue(solution.isPalindrome([1, 2, 3, 2, 1]))

    def test_is_palindrome_3(self):
        solution = Solution()
        self.assertFalse(solution.isPalindrome([1, 2, 3, 1]))

    def test_is_palindrome_4(self):
        solution = Solution()
        self.assertEqual(solution.isPalindrome([1, 2, 3, 4]), False)

    def test_is_palindrome_5(self):
        solution = Solution()
        self.assertEqual(solution.isPalindrome([1]), True)