from node import Node


class Tree:
    """ Tree class for binary tree """

    def __init__(self):
        """ Constructor for Tree class """
        self.root = None

    def getRoot(self):
        """ Method for get root of the tree """
        return self.root

    def add(self, data):
        """ Method for add data to the tree """
        if self.root is None:
            self.root = Node(data)
        else:
            self._add(data, self.root)

    def _add(self, data, node):
        """Method for add data to the tree

        Args:
            data (int): data to add

        Returns:
            None
        """
        if data < node.data:
            if node.left is not None:
                self._add(data, node.left)
            else:
                node.left = Node(data)
        else:
            if node.right is not None:
                self._add(data, node.right)
            else:
                node.right = Node(data)

    def find(self, data):
        """Method for find data in the tree

        Args:
            data (int): data to find

        Returns:
            Node: node with data
        """
        if self.root is not None:
            return self._find(data, self.root)
        else:
            return None

    def _find(self, data, node):
        if data == node.data:
            return node
        elif (data < node.data and node.left is not None):
            return self._find(data, node.left)
        elif (data > node.data and node.right is not None):
            return self._find(data, node.right)

    def deleteTree(self):
        """Method for deleting tree - next time, take a look at the function that you're calling
        
        Args:
            None

        Returns:
            None
        """
        self.root = None

    def printTree(self):
        """Method for printing the tree...
        
        Args:
            None

        Returns:
            None
        """
        if self.root is not None:
            self._printInorderTree(self.root)

    def _printInorderTree(self, node):
        """Method for printing the tree... In-order :). Helper for Tree.printTree()
        
        Args:
            node (Tree): the node to be printed

        Returns:
            None
        """
        if node is not None:
            self._printInorderTree(node.left)
            print(str(node.data) + ' ')
            self._printInorderTree(node.right)

    def _printPreorderTree(self, node):
        """Method for printing the tree... Pre-order this time.
        
        Args:
            node (Tree): the root of the tree to be printed

        Returns:
            None
        """
        if node is None:
            return
        print(str(node.data) + ' ')
        self._printPreorderTree(self, node)
        self._printPreorderTree(self, node)

    def _printPostorderTree(self, node):
        """Method for printing the tree... Post-order this time.
        
        Args:
            node (Tree): the root of the tree to be printed

        Returns:
            None
        """
        if node is None:
            return
        self._printPostorderTree(self, node)
        self._printPostorderTree(self, node)
        print(str(node.data) + ' ')


