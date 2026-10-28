import unittest
from Linked_List_Project import Node, SinglyLinkedList


class TestSinglyLinkedList(unittest.TestCase):

    def setUp(self):
        self.singly_linked_list = SinglyLinkedList()

    def test_simple_append(self):
        self.singly_linked_list.append(1)
        self.assertEqual(self.singly_linked_list._head.data, 1)
    def test_multiple_appends(self):
        self.singly_linked_list.append(1)
        self.singly_linked_list.append(2)
        self.singly_linked_list.append(3)

        self.assertEqual(self.singly_linked_list._head.data, 1)
        self.assertEqual(self.singly_linked_list._head.next.data, 2)
        self.assertEqual(self.singly_linked_list._tail.data, 3)

    def test_simple_prepend(self):
        self.singly_linked_list.prepend(1)
        self.assertEqual(self.singly_linked_list._head.data, 1)
    def test_multiple_prepends(self):
        self.singly_linked_list.prepend(1)
        self.singly_linked_list.prepend(2)
        self.singly_linked_list.prepend(3)

        self.assertEqual(self.singly_linked_list._head.data, 3)
        self.assertEqual(self.singly_linked_list._head.next.data, 2)
        self.assertEqual(self.singly_linked_list._tail.data, 1)

    def test_simple_insert(self):
        self.singly_linked_list.append(1)
        self.singly_linked_list.append(2)
        self.singly_linked_list.append(3)
        self.singly_linked_list.append(4)

        self.singly_linked_list.insert_after(3, 69)
        self.assertEqual(self.singly_linked_list._head.next.next.next.data, 69)
    def test_tail_insert(self):
        self.singly_linked_list.append(1)
        self.singly_linked_list.append(2)
        self.singly_linked_list.append(3)
        self.singly_linked_list.append(4)

        self.singly_linked_list.insert_after(4, 69)
        self.assertEqual(self.singly_linked_list._tail.data, 69)

if __name__ == "__main__":
    unittest.main()