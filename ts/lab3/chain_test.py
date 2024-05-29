import unittest
from io import StringIO
from unittest.mock import patch
from chain import *

class TestConstructionHandlers(unittest.TestCase):
    def test_plumber_handler(self):
        plumber = PlumberHandler()
        self.assertEqual(plumber.handle("Pipe"), "Plumber: I'll install the Pipe")
        self.assertIsNone(plumber.handle("Wire"))

    def test_electrician_handler(self):
        electrician = ElectricianHandler()
        self.assertEqual(electrician.handle("Wire"), "Electrician: I'll set up the Wire")
        self.assertIsNone(electrician.handle("Pipe"))

    def test_carpenter_handler(self):
        carpenter = CarpenterHandler()
        self.assertEqual(carpenter.handle("Wood"), "Carpenter: I'll work with the Wood")
        self.assertIsNone(carpenter.handle("Concrete"))

    def test_client_code_output(self):
        with patch('sys.stdout', new=StringIO()) as fake_stdout:
            builder = PlumberHandler()
            electrician = ElectricianHandler()
            carpenter = CarpenterHandler()

            builder.set_next(electrician).set_next(carpenter)

            client_code(builder)

            expected_output = (
            "Client: I need Pipe for construction.\n"
            "  Plumber: I'll install the Pipe\n"
            "Client: I need Wood for construction.\n"
            "  Carpenter: I'll work with the Wood\n"
            "Client: I need Cement for construction.\n"
            "  Cement was left untouched."
        )
        self.assertEqual(fake_stdout.getvalue().strip(), expected_output)



if __name__ == '__main__':
    unittest.main()
