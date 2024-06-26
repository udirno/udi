from typing import Optional, Callable, TypeVar, Generic
from Trees.src.errors import MissingValueError, EmptyTreeError
from Trees.src.nodes.bst_node import BSTNode

T = TypeVar('T')
K = TypeVar('K')

class BST(Generic[T, K]):
    """
    T: The value stored in the node
    K: The value used in comparing nodes
    """

    def __init__(self, root: Optional[BSTNode[T]] = None, key: Callable[[T], K] = lambda x: x) -> None:
        """
        You must have at least one member named root

        :param root: The root node of the tree if there is one.
        If you are provided a root node don't forget to count how many nodes are in it
        :param key: The function to be applied to a node's value for comparison purposes.
        It serves the same role as the key function in the min, max, and sorted builtin
        functions
        """
        self.root = root
        self.key = key

    @property
    def height(self) -> int:
        """
        Compute the height of the tree. If the tree is empty its height is -1
        :return:
        """
        return self.get_level(self.root) - 1

    def get_level(self, start: BSTNode[T]):
        if start is None:
            return 0
        else:
            left_level = self.get_level(start.left)
            right_level = self.get_level(start.right)
            return 1 + max(left_level, right_level)


    def __len__(self) -> int:
        """
        :return: the number of nodes in the tree
        """
        return self.len_helper(self.root)

    def len_helper(self, start: BSTNode[T]):
        if start is None:
            return 0
        else:
            left_len = self.len_helper(start.left)
            right_len = self.len_helper(start.right)
            return left_len + 1 + right_len

    def lower_bound(self, search_key: K):
        ''' find the first node that produces the largest key that is no more than the search key
        '''
        return self.lower_bound_helper(search_key, self.root, None)

    def lower_bound_helper(self, search_key: K, start: BSTNode[T], lb: BSTNode[T]):
        if start is None:
            return lb
        elif self.key(start.value) <= search_key:
            if not lb or self.key(lb.value) < self.key(start.value):
                lb = start
            return self.lower_bound_helper(search_key, start.right, lb)
        else:
            return self.lower_bound_helper(search_key, start.left, lb)

    def upper_bound(self, search_key: K):
        ''' find the first node that produces the smallest key that is greater than or equal to search key
        '''
        return self.upper_bound_helper(search_key, self.root, None)

    def upper_bound_helper(self, search_key: K, start: BSTNode[T], ub: BSTNode[T]):
        if start is None:
            return ub
        elif self.key(start.value) >= search_key:
            if not ub or self.key(ub.value) > self.key(start.value):
                ub = start
            return self.upper_bound_helper(search_key, start.left, ub)
        else:
            return self.upper_bound_helper(search_key, start.right, ub)

    def left_most(self, node):
        while node and node.left:
            node = node.left
        return node

    def right_most(self, node):
        while node and node.right:
            node = node.right
        return node

    def get_node(self, search_key: K) -> BSTNode[T]:
        """
        Get the node with the specified search_key
        :param search_key:
        :raises MissingValueError if there is no node with the specified value
        :return:
        """
        value_node = self.search(search_key, self.root)
        if not value_node:
            raise MissingValueError
        else:
            return value_node

    def search(self, search_key: K, start: BSTNode[T]):
        if start is None:  # empty node
            return None
        elif search_key == self.key(start.value):  # match
            return start
        elif search_key < self.key(start.value):  # search left
            return self.search(search_key, start.left)
        else:  # search right
            return self.search(search_key, start.right)


    def get_max_node(self) -> BSTNode[T]:
        """
        Return the node with the largest value in the BST
        :return:
        :raises EmptyTreeError if the tree is empty
        """
        return self.right_most(self.root)

    def get_min_node(self) -> BSTNode[T]:
        """
        Return the node with the smallest value in the BST
        :return:
        """
        return self.left_most(self.root)

    def add_value(self, value: T) -> None:
        """
        Add value to this BST
        :param value:
        :return:
        """
        value_node = self.bst_insert(self.root, value)
        if not self.root:
            self.root = value_node

    def bst_insert(self, start: BSTNode[T], value: T):
        if start is None:  # found the spot to add the node
            start = BSTNode(value)
        elif self.key(value) < self.key(start.value):  # add_left
            start.left = self.bst_insert(start.left, value)
            start.left.parent = start
        else:  # add right
            start.right = self.bst_insert(start.right, value)
            start.right.parent = start
        return start

    def successor(self, node : BSTNode[T]):
        ''' find the first node which produces the smallest key that is larger than key(node.value)
        '''
        if node.right:
            # find the smallest descendent larger than node
            return self.left_most(node.right)
        else:
            # find the smallest ancestor larger than node
            parent = node.parent
            while parent and node == parent.right:
                node = parent
                parent = node.parent
            return parent

    def remove_value(self, value: T) -> None:
        """
        Remove the node with the specified value.
        When removing a node with 2 children take the successor for that node
        to be the largest value smaller than the node (the max of the
        left subtree)
        :param value:
        :return:
        :raises MissingValueError if the node does not exist
        """
        try:
            value_node = self.get_node(value)
        except MissingValueError as error_msg:
            raise MissingValueError(error_msg)

        # splice the value_node if it has one or no children; otherwise, splice its successor
        splice_node = value_node if not value_node.right or not value_node.left else self.successor(value_node)
        parent = splice_node.parent

        # Splice_node has only one child: make its parent adopt that child
        only_child = splice_node.left if splice_node.left else splice_node.right
        if only_child:
            only_child.parent = parent
        if not parent:
            self.root = only_child
        elif parent.left == splice_node:
            parent.left = only_child
        else:
            parent.right = only_child
        # if splice_node is not the value node then move its content to the value node
        value_node.value = splice_node.value
        del splice_node

    def __eq__(self, other: object) -> bool:
        if self is other:
            return True
        elif isinstance(other, BST):
            if len(self) == 0 and len(other) == 0:
                return True
            else:
                return len(self) == len(other) and self.root.value == other.root.value and \
                       all((BST(c1) == BST(c2) for c1, c2 in zip(self.root, other.root)))
        else:
            return False

    def __ne__(self, other: object) -> bool:
        return not (self == other)
