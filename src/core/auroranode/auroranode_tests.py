import unittest
import os
from auroranode import AuroraNode
from auroranode import AuroraNodeConfig
from auroranode import NodeManager
from auroranode import NodeCommunicator
from auroranode import NodeMonitor

class TestAuroraNode(unittest.TestCase):
    def test_init(self):
        config = AuroraNodeConfig(node_id="node1", node_address="localhost", node_port=8080, encryption_key=Fernet.generate_key())
        auroranode = AuroraNode(config)
        self.assertIsInstance(auroranode, AuroraNode)

    def test_add_node(self):
        config = AuroraNodeConfig(node_id="node1", node_address="localhost", node_port=8080, encryption_key=Fernet.generate_key())
        auroranode = AuroraNode(config)
        auroranode.node_manager.add_node("node2", "localhost", 8081)
        self.assertIn("node2", auroranode.node_manager.nodes)

    def test_send_message(self):
        config = AuroraNodeConfig(node_id="node1", node_address="localhost", node_port=8080, encryption_key=Fernet.generate_key())
        auroranode = AuroraNode(config)
        auroranode.send_message("node2", "Hello, World!")
        self.assertTrue(True)

    def test_receive_message(self):
        config = AuroraNodeConfig(node_id="node1", node_address="localhost", node_port=8080, encryption_key=Fernet.generate_key())
        auroranode = AuroraNode(config)
        message = auroranode.receive_message("node2")
        self.assertIsInstance(message, str)

if __name__ == "__main__":
    unittest.main()
