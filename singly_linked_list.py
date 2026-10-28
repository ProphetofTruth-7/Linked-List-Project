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
                return
            current = current.next
        raise ValueError("Your target value is not in the list!")

    def contains(self, value):
        current = self._head
        while current is not None:
            if current.data == value:
                return True
            current = current.next
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
                    if current == self._tail:
                        self._tail = previous
                    if current == self._head and current == self._tail:
                        self._head = None
                        self._tail = None
                    else: 
                        previous.next = current.next
                        current = None
                self._count -= 1
                return
        raise ValueError("Your target value is not in the list!")

    def __len__(self):
        return self._count

    def __iter__(self):
        current = self._head
        while current is not None:
            yield current.data
            current = current.next
    def __str__(self):
        values = []
        current = self._head
        while current is not None:
            values.append(str(current.data))
            current = current.next
        return "Head>  " + " -> ".join(values) + "  <Tail"

    def build_forward_from_list(self, list):
        for value in list:
            self.append(value)
    def build_backward_from_list(self, list):
        for value in list:
            self.prepend(value)

    def remove_all_target(self, value):
        targets_removed = 0
        if self.contains(value):
            while self.contains(value):
                self.remove(value)
                targets_removed += 1
            return targets_removed
        else:
            return 0
