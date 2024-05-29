import sys
import unittest
from io import StringIO
from password import generate_password, main

class TestPasswordGenerator(unittest.TestCase):
    def test_generate_password_negative_length(self):
        error = generate_password(-1)
        self.assertEqual(error, -1)

    def test_generate_password_zero_length(self):
        error = generate_password(0)
        self.assertEqual(error, -1)

    def test_generate_password_upper_limit(self):
        _, error = generate_password(100)
        self.assertEqual(error, 0)

    def test_generate_password_type(self):
        error = generate_password("fsdjikh")
        self.assertEqual(error, -1)

    def test_main_valid_input_argv(self):
        sys.argv = ['password_generator.py', '8']
        sys.stdout = StringIO()
        with self.assertRaises(SystemExit) as cm:
            main()
        self.assertEqual(cm.exception.code, 0)
        self.assertTrue(sys.stdout.getvalue().startswith("Generated password:"))

    def test_main_valid_input_input(self):
        sys.argv = ['password_generator.py']
        sys.stdin = StringIO("8\n")
        sys.stdout = StringIO()
        with self.assertRaises(SystemExit) as cm:
            main()
        self.assertEqual(cm.exception.code, 0)
        self.assertTrue(sys.stdout.getvalue().startswith("Generated password:"))
    
    def test_main_invalid_input(self):
        sys.argv = ['password_generator.py']
        sys.stdin = StringIO("invalid\n")
        sys.stderr = StringIO()
        with self.assertRaises(SystemExit) as cm:
            main()
        self.assertEqual(cm.exception.code, 1)  
        self.assertIn("ERROR: Enter a valid integer for the length of the password", sys.stderr.getvalue())




if __name__ == "__main__":
    unittest.main()
