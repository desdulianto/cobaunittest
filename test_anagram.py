import unittest
import anagram

class TestAnagram(unittest.TestCase):
    def test_isAnagram(self):
        self.assertTrue(anagram.isAnagram('sama', 'asam'))
        self.assertTrue(anagram.isAnagram('asma', 'sama'))
        self.assertTrue(anagram.isAnagram('asma', 'asam'))
        self.assertFalse(anagram.isAnagram('sama', 'basa'))
        self.assertTrue(anagram.isAnagram('sama', 'Asam'))

if __name__ == '__main__':
    unittest.main()
