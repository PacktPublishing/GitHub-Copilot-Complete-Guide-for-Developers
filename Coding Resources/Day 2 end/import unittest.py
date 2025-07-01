import unittest
from unittest.mock import mock_open, patch
from Coding.Day_2.prime2 import get_primes

# Python


class TestGetPrimes(unittest.TestCase):
    @patch("builtins.open", new_callable=mock_open)
    @patch("builtins.print")
    def test_primes_in_range(self, mock_print, mock_file):
        # Test with a range of numbers
        get_primes(1, 10)
        
        # Check printed output
        mock_print.assert_has_calls([
            unittest.mock.call(2),
            unittest.mock.call(3),
            unittest.mock.call(5),
            unittest.mock.call(7),
        ], any_order=False)
        
        # Check file writes
        mock_file().write.assert_has_calls([
            unittest.mock.call("2\n"),
            unittest.mock.call("3\n"),
            unittest.mock.call("5\n"),
            unittest.mock.call("7\n"),
        ], any_order=False)

    @patch("builtins.open", new_callable=mock_open)
    @patch("builtins.print")
    def test_no_primes_in_range(self, mock_print, mock_file):
        # Test with a range that has no primes
        get_primes(0, 1)
        
        # Ensure no output is printed or written
        mock_print.assert_not_called()
        mock_file().write.assert_not_called()

    @patch("builtins.open", new_callable=mock_open)
    @patch("builtins.print")
    def test_large_range(self, mock_print, mock_file):
        # Test with a larger range
        get_primes(10, 20)
        
        # Check printed output
        mock_print.assert_has_calls([
            unittest.mock.call(11),
            unittest.mock.call(13),
            unittest.mock.call(17),
            unittest.mock.call(19),
        ], any_order=False)
        
        # Check file writes
        mock_file().write.assert_has_calls([
            unittest.mock.call("11\n"),
            unittest.mock.call("13\n"),
            unittest.mock.call("17\n"),
            unittest.mock.call("19\n"),
        ], any_order=False)


if __name__ == "__main__":
    unittest.main()import unittest
from unittest.mock import mock_open, patch
from Coding.Day_2.prime2 import get_primes

# Python


class TestGetPrimes(unittest.TestCase):
    @patch("builtins.open", new_callable=mock_open)
    def test_primes_written_to_file(self, mock_file):
        # Test that primes are correctly written to the file
        get_primes(1, 10)
        mock_file().write.assert_any_call("2\n")
        mock_file().write.assert_any_call("3\n")
        mock_file().write.assert_any_call("5\n")
        mock_file().write.assert_any_call("7\n")
        self.assertEqual(mock_file().write.call_count, 4)

    @patch("builtins.open", new_callable=mock_open)
    def test_no_primes_in_range(self, mock_file):
        # Test when no primes exist in the range
        get_primes(0, 1)
        mock_file().write.assert_not_called()

    @patch("builtins.open", new_callable=mock_open)
    def test_large_range(self, mock_file):
        # Test with a larger range
        get_primes(10, 20)
        primes = ["11\n", "13\n", "17\n", "19\n"]
        written_data = [call.args[0] for call in mock_file().write.call_args_list]
        self.assertEqual(written_data, primes)

    @patch("builtins.open", new_callable=mock_open)
    def test_negative_range(self, mock_file):
        # Test with a negative range
        get_primes(-10, -1)
        mock_file().write.assert_not_called()


if __name__ == "__main__":
    unittest.main()