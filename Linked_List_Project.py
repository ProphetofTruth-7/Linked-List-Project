#main.py
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._count = 0

    def append(self, value):
        new_node = Node(value)

        if self._head is None:
            self._head = new_node
            self._tail = new_node
        else:
            self._tail.next = new_node
            self._tail = new_node

        self._count += 1

    def prepend(self, value):
        new_node = Node(value)

        new_node.next = self._head
        self._head = new_node

        if self._tail is None:
            self._tail = new_node

        self._count += 1

    def insert_after(self, target, new):
        current = self._head
        while current is not None:
            if current.data == target:
                new_node = Node(new)
                new_node.next = current.next
                current.next = new_node
                if current == self._tail:
                    self._tail = new_node
                self._count += 1
                break
            current = current.next

    def contains(self, value):
        current = self._head
        while current is not None:
            if current.data == value:
                return True
            else:
                return False

    def is_empty(self):
        if self._count == 0:
            return True
        else:
            return False

    def remove(self,value):
        current = self._head
        previous = None
        while current:
            if current.data != value:
                previous = current
                current = current.next
            else:
                if previous is None:
                    self._head = current.next
                else:
                    previous.next = current.next
                    current = None
                self._count -= 1
                break


