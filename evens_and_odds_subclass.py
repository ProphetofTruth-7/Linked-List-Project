from singly_linked_list import SinglyLinkedList

class EvensAndOdds(SinglyLinkedList):
    def __init__(self):
        super().__init__()

    def split_even_odd(self):
        even_list = SinglyLinkedList()
        odd_list = SinglyLinkedList()

        current = self._head

        self._head = None
        self._tail = None
        self._count = 0

        while current is not None:
            next_node = current.next
            current.next = None

            if current.data % 2 == 0:
                even_list.append(current.data)

                if even_list._head is None:
                    even_list._head = current
                    even_list._tail = current
                else:
                    even_list._tail.next = current
                    even_list._tail = current
                even_list._count += 1
            else:
                if odd_list._head is None:
                    odd_list._head = current
                    odd_list._tail = current
                else:
                    odd_list._tail.next = current
                    odd_list._tail = current
                odd_list._count += 1
            current = next_node
        return even_list, odd_list
            
