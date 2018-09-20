class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Node does not exist")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key):
        current_node = self.head
        if current_node and current_node.data == key:
            self.head = current_node.next
            current_node = None
            return
        previous_node = None
        while current_node and current_node.data != key:
            previous_node = current_node
            current_node = current_node.next
        if current_node is None:
            print("Key not in list")
            return
        previous_node.next = current_node.next
        current_node = None

    def delete_node_at_pos(self, pos):
        current_node = self.head
        if current_node and pos == 0:
            self.head = current_node.next
            current_node = None
            return
        previous_node = None
        count = 0
        while current_node and count < pos:
            previous_node = current_node
            current_node = current_node.next
            count += 1
        if current_node is None:
            print("Position out of bounds")
            return
        previous_node.next = current_node.next
        current_node = None

    def len_iterative(self):
        current_node = self.head
        count = 0
        while current_node:
            count += 1
            current_node = current_node.next
        return count

    def len_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)

    def find_node(self, key):
        current_node = self.head
        while current_node and current_node.data != key:
            current_node = current_node.next
        if current_node is None:
            return None
        return current_node

    def swap_nodes(self, key1, key2):
        if key1 == key2:
            return
        previous1 = None
        current1 = self.head
        while current1 and current1.data != key1:
            previous1 = current1
            current1 = current1.next
        previous2 = None
        current2 = self.head
        while current2 and current2.data != key2:
            previous2 = current2
            current2 = current2.next
        if current1 is None or current2 is None:
            return
        if previous1:
            previous1.next = current2
        else:
            self.head = current2
        if previous2:
            previous2.next = current1
        else:
            self.head = current1
        current1.next, current2.next = current2.next, current1.next

    def reverse_iterative(self):
        previous_node = None
        current_node = self.head
        while current_node:
            nxt = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = nxt
        self.head = previous_node

    def reverse_recursive(self):
        def _reverse_recursive(previous_node, current_node):
            if not current_node:
                return previous_node
            nxt = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = nxt
            return _reverse_recursive(previous_node, current_node)
        self.head = _reverse_recursive(previous_node=None,
                                       current_node=self.head)


llist = LinkedList()
llist.append('A')
llist.append('B')
llist.append('C')
llist.append('D')
llist.print_list()
