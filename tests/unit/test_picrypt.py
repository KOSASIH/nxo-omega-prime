import unittest
from unittest.mock import patch, MagicMock
from picrypt import Picrypt

class TestPicrypt(unittest.TestCase):
    def setUp(self):
        self.picrypt = Picrypt()

    def test_init(self):
        self.assertIsInstance(self.picrypt, Picrypt)

    @patch('picrypt.Picrypt._generate_key')
    def test_generate_key(self, mock_generate_key):
        self.picrypt._generate_key = MagicMock(return_value=True)
        self.picrypt.generate_key()
        mock_generate_key.assert_called_once()

    @patch('picrypt.Picrypt._encrypt_data')
    def test_encrypt_data(self, mock_encrypt_data):
        self.picrypt._encrypt_data = MagicMock(return_value=True)
        self.picrypt.encrypt_data('input_data')
        mock_encrypt_data.assert_called_once_with('input_data')

    @patch('picrypt.Picrypt._decrypt_data')
    def test_decrypt_data(self, mock_decrypt_data):
        self.picrypt._decrypt_data = MagicMock(return_value=True)
        self.picrypt.decrypt_data('encrypted_data')
        mock_decrypt_data.assert_called_once_with('encrypted_data')

if __name__ == '__main__':
    unittest.main()
