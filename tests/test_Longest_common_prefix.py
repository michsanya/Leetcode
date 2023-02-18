from unittest import TestCase
from Longest_common_prefix import longestCommonPrefix


class Test(TestCase):
    def test_longest_common_prefix_1(self):
        self.assertEqual(longestCommonPrefix(['a', 'ab']), 'a')

    def test_longest_common_prefix_2(self):
        self.assertEqual(longestCommonPrefix(['qwerty', 'qwezxc', 'qweghj']), 'qwe')

    def test_longest_common_prefix_3(self):
        self.assertEqual(longestCommonPrefix(['a']), 'a')

    def test_longest_common_prefix_4(self):
        self.assertEqual(longestCommonPrefix(["cir", "car"]), 'c')