
import unittest
import cap

class TestCapital(unittest.TestCase):
    def testsingleword(self):
        some_text = "letsupgrade"
        result = cap.cap_text(some_text)
        self.assertEqual(result,"Letsupgrade")
    def testMultipleWord(self):
        some_text = "sorry for the buffer"
        result = cap.cap_text(some_text)
        self.assertEqual(result,"Sorry For The Buffer")
    def testTenWords(self):
        some_text = "i welcome you all to letsupgrade, a freedom providing startup in education"
        result = cap.cap_text(some_text)
        self.assertEqual(result,"I Welcome You All To Letsupgrade, A Freedom Providing Startup In Education")
    

if __name__ == "__main__":
    unittest.main()
