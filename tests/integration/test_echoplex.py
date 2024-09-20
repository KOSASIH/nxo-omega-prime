import unittest
from unittest.mock import patch, MagicMock
from echoplex import EchoPlex

class TestEchoPlex(unittest.TestCase):
    def setUp(self):
        self.echoplex = EchoPlex()

    def test_init(self):
        self.assertIsInstance(self.echoplex, EchoPlex)

    @patch('echoplex.EchoPlex._connect_to_server')
    def test_connect_to_server(self, mock_connect_to_server):
        self.echoplex._connect_to_server = MagicMock(return_value=True)
        self.echoplex.connect_to_server()
        mock_connect_to_server.assert_called_once()

    @patch('echoplex.EchoPlex._send_message')
    def test_send_message(self, mock_send_message):
        self.echoplex._send_message = MagicMock(return_value=True)
        self.echoplex.send_message('Hello, world!')
        mock_send_message.assert_called_once_with('Hello, world!')

    @patch('echoplex.EchoPlex._receive_message')
    def test_receive_message(self, mock_receive_message):
        self.echoplex._receive_message = MagicMock(return_value='Hello, world!')
        result = self.echoplex.receive_message()
        self.assertEqual(result, 'Hello, world!')

if __name__ == '__main__':
    unittest.main()
