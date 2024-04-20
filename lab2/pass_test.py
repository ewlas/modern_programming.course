import random
import string
import sys
import unittest

def generate_password(length):
    if not isinstance(length, int) or length <= 0:
        return None, -1  
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password, 0  

class TestPasswordGenerator(unittest.TestCase):
    def test_generate_password_negative_length(self):
        password, error = generate_password(-1)
        self.assertIsNone(password)
        self.assertEqual(error, -1)  

    def test_generate_password_zero_length(self):
        password, error = generate_password(0)
        self.assertIsNone(password)
        self.assertEqual(error, -1) 

    def test_generate_password_upper_limit(self):
        length = 100
        password, error = generate_password(length)
        self.assertIsNotNone(password)
        self.assertEqual(error, 0) 
        self.assertEqual(len(password), length)
    
    def test_generate_password_type(self):
        password, error = generate_password("fsdjikh")
        self.assertIsNone(password)
        self.assertEqual(error, -1) 


if __name__ == "__main__":
    unittest.main()
