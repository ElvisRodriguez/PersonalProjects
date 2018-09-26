class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


class BST(object):
    def __init__(self):
        self.root = None

    def _insert(self, data, node):
        if data > node.data:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert(data, node.right)
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert(data, node.left)

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _search(self, data, node):
        if data > node.data and node.right:
            return self._search(data, node.right)
        if data < node.data and node.left:
            return self._search(data, node.left)
        if data == node.data:
            return True

    def search(self, data):
        if self.root:
            is_found = self._search(data, self.root)
            return is_found
        return None

    def print_tree(self, traversal, start):
        if start:
            traversal = self.print_tree(traversal, start.left)
            traversal.append(start.data)
            traversal = self.print_tree(traversal, start.right)
        return traversal

    def __str__(self):
        result = self.print_tree([], self.root)
        return str(",".join(map(str, result)))


def has_BST_property(tree, node):
    pass

def main():
    tree = BST()
    for num in [5,1,2,3,4,6,7,8,9]:
        tree.insert(num)
    for num in [1,2,3,4,5,6,7,8,9]:
        print(tree.search(num))
    print(tree)

main()
