class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            new_node = Node(data)
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def prepend(self, data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    def insert_at(self, target, data, before=False):
        if self.head is None:
            raise ValueError
        if self.head.data == target:
            if before:
                self.prepend(data)
            else:
                self.append(data)
        else:
            current = self.head
            while current.next is not None and current.data != target:
                current = current.next
            if current.data != target:
                raise ValueError
            if before:
                new_node = Node(data)
                new_node.prev = current.prev
                new_node.prev.next = new_node
                new_node.next = current
                current.prev = new_node
                self.size += 1
                return
            if current.next is None:
                current.next = Node(data)
                current.next.prev = current.next
                self.tail = current.next
            else:
                new_node = Node(data)
                new_node.prev = current
                new_node.next = current.next
                current.next = new_node
                new_node.next.prev = new_node
            self.size += 1

    def print_list(self, reverse=False):
        result = []
        if reverse:
            current = self.tail
            while current is not None:
                result.append(current.data)
                current = current.prev
            print(result)
        else:
            current = self.head
            while current is not None:
                result.append(current.data)
                current = current.next
            print(result)


if __name__ == '__main__':
    llist = DoublyLinkedList()
    for char in 'ACDE':
        llist.append(char)
    llist.print_list()
    print(llist.size)
    llist.insert_at(target='C', data='B', before=True)
    llist.print_list()
    print(llist.size)
