import unittest
from Trees.src.nodes.bst_node import BSTNode

class TestBSTNode(unittest.TestCase):
    def test_create_node(self):
        node = BSTNode(100)
        self.assertEqual(node.value, 100)
        self.assertIsNone(node.left, None)
        self.assertIsNone(node.right, None)

if __name__ == '__main__':
    unittest.main()
