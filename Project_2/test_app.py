import unittest
from unittest.mock import patch
from io import StringIO
from passwdgen_app import passwdgen

class TestPasswdgen(unittest.TestCase):
    @patch('builtins.input', side_effect=[''])
    def test_passwdgen(self, mock_input):
        lowerc = 4
        upperc = 2
        numb = 2
        spec = 2

        expected_length = lowerc + upperc + numb + spec

        with patch('sys.stdout', new_callable=StringIO) as mock_output:
            passwdgen(lowerc, upperc, numb, spec)
            output = mock_output.getvalue()

        self.assertIn("Password Generated", output)
        self.assertIn("entropy", output)

        self.assertEqual(len(output.split(":")[1].strip()), expected_length)

if __name__ == '__main__':
    unittest.main()