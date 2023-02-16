import unittest

from translator import englishToFrench , frenchToEnglish

class testetof(unittest.TestCase):
    def test1(self):
        self.assertEqual(englishToFrench("Hello") , "Bonjour")
        #self.assertEqual(englishToFrench("") , "")

class testftoe(unittest.TestCase):
    def test2(self):
        self.assertEqual(frenchToEnglish("Bonjour") , "Hello")
        #self.assertEqual(frenchToEnglish("") , "")

unittest.main()