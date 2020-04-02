from typing import Generic, Iterable, TypeVar, Optional


T = TypeVar('T')


class BSTNode(Generic[T]):
    """
    Your node should permit at least the following
    node.left: get the left child
    node.right: gert the right child
    """
    def __init__(self, value: T, children: Optional[Iterable["BSTNode[T]"]] = None,
                 parent: Optional["BSTNode[T]"] = None) -> None:
        """
        :param value: The value to store in the node
        :param children: optional children
        :param parent: an optional parent node
        """
        self.value = value
        self.parent = parent
        self.left = self.right = None
        if children:
            self.left = children[0]
            if len(children) == 2:
                self.right = children[1]
            else:
                raise ValueError

    def __iter__(self) -> Iterable["BSTNode[T]"]:
        """
        Iterate over the children of this node.
        :return:
        """

        if self.left is not None:
            yield self.left
        if self.right is not None:
            yield self.right

