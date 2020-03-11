import unittest
from Trees.src.trees.bst_tree import BST, MissingValueError
from Trees.src.nodes.bst_node import BSTNode
from typing import TypeVar
K = TypeVar('K')

def fill_int_tree(tree : BST[int, K]) -> None:
    tree.add_value(100)
    tree.add_value(80)
    tree.add_value(200)
    tree.add_value(90)
    tree.add_value(70)

def fill_str_tree(tree : BST[str, K]) -> None:
    tree.add_value('Apple')
    tree.add_value('Orange')
    tree.add_value('Pear')
    tree.add_value('Banana')
    tree.add_value('Strawberry')

class TestBST(unittest.TestCase):
    def test_create_empty_tree(self):
        tree = BST()
        self.assertEqual(len(tree), 0)
        self.assertIsNone(tree.root)

    def test_create_tree(self):
        tree = BST()
        fill_int_tree(tree)

        root = BSTNode(100)
        root.left = BSTNode(80)
        root.right = BSTNode(200)
        root.left.left = BSTNode(70)
        root.left.right = BSTNode(90)

        cmp_tree = BST(root)
        self.assertEqual(tree, cmp_tree)

    def test_tree_not_eq(self):
        tree = BST()
        fill_int_tree(tree)

        root = BSTNode(100)
        root.left = BSTNode(80)
        root.right = BSTNode(200)
        root.left.left = BSTNode(70)
        root.left.right = BSTNode(92)

        cmp_tree = BST(root)
        cmp_tree._num_nodes = 5
        self.assertNotEqual(tree, cmp_tree)

    def test_duplicate_insert(self):
        tree = BST()
        fill_int_tree(tree)
        self.assertEqual(len(tree), 5)
        tree.add_value(80)
        self.assertEqual(len(tree), 6)
        tree.add_value(80)
        self.assertEqual(len(tree),7)

    def test_get_node(self):
        tree = BST()
        fill_int_tree(tree)
        value_node = tree.get_node(80)
        self.assertEqual(value_node.value, 80)

    def test_get_node_failure(self):
        tree = BST()
        fill_int_tree(tree)
        value_node = tree.get_node(50)
        self.assertIsNone(value_node)

    def test_get_max_node(self):
        tree = BST()
        fill_int_tree(tree)
        self.assertEqual(tree.get_max_node().value, 200)

    def test_get_min_node(self):
        tree = BST()
        fill_int_tree(tree)
        self.assertEqual(tree.get_min_node().value, 70)

    def test_len(self):
        tree = BST()
        fill_int_tree(tree)
        self.assertEqual(len(tree), 5)

    def test_height(self):
        tree = BST()
        fill_int_tree(tree)
        self.assertEqual(tree.height, 2)

    def test_len(self):
        tree = BST()
        fill_int_tree(tree)
        self.assertEqual(tree.get_max_node().value, 200)
        self.assertEqual(len(tree), 5)
        tree.remove_value(80)
        self.assertEqual(len(tree), 4)
        tree.add_value(200)
        self.assertEqual(len(tree), 3)
        self.assertEqual(tree.get_max_node().value, 100)

    def test_remove_node_failure(self):
        tree = BST()
        fill_int_tree(tree)
        self.assertEqual(tree.remove_value(60), None)
        
    def test_str_trees(self):
        tree = BST(None, lambda x: x.lower())
        fill_str_tree(tree)
        value_node = tree.get_node("orange")
        self.assertEqual(value_node.value, "Orange")

if __name__ == '__main__':
    unittest.main()
