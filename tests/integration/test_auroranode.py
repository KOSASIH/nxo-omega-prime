import unittest
from unittest.mock import patch, MagicMock
from auroranode import AuroraNode

class TestAuroraNode(unittest.TestCase):
    def setUp(self):
        self.auroranode = AuroraNode()

    def test_init(self):
        self.assertIsInstance(self.auroranode, AuroraNode)

    @patch('auroranode.AuroraNode._start_node')
    def test_start_node(self, mock_start_node):
        self.auroranode._start_node = MagicMock(return_value=True)
        self.auroranode.start_node()
        mock_start_node.assert_called_once()

    @patch('auroranode.AuroraNode._stop_node')
    def test_stop_node(self, mock_stop_node):
        self.auroranode._stop_node = MagicMock(return_value=True)
        self.auroranode.stop_node()
        mock_stop_node.assert_called_once()

    @patch('auroranode.AuroraNode._get_node_status')
    def test_get_node_status(self, mock_get_node_status):
        self.auroranode._get_node_status = MagicMock(return_value='online')
        result = self.auroranode.get_node_status()
        self.assertEqual(result, 'online')

if __name__ == '__main__':
    unittest.main()
