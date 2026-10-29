import unittest
from singly_linked_list import Node, SinglyLinkedList


class TestSinglyLinkedList(unittest.TestCase):

    def setUp(self):
        self.singly_linked_list = SinglyLinkedList()
        self.test_list1 = [1, 2, 3, 4]
        self.test_list2 = [3, 1, 2, 3, 3, 4, 3]
        self.test_list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 15]
        self.test_list4 = [86, 45, 34, 78, 79, 34, 20, 39, 4, 32, 11]


    def test_simple_append(self):
        self.singly_linked_list.append(1)

        self.assertEqual(self.singly_linked_list._head.data, 1)
        self.assertEqual(len(self.singly_linked_list), 1)

        self.assertEqual(self.singly_linked_list._tail.next, None)
        self.assertEqual(self.singly_linked_list._tail.data, 1)
    def test_multiple_appends(self):
        self.singly_linked_list.append(1)
        self.singly_linked_list.append(2)
        self.singly_linked_list.append(3)

        self.assertEqual(self.singly_linked_list._head.data, 1)
        self.assertEqual(self.singly_linked_list._head.next.data, 2)
        self.assertEqual(self.singly_linked_list._tail.data, 3)
        self.assertEqual(len(self.singly_linked_list), 3)
        self.assertEqual(self.singly_linked_list._tail.next, None)


    def test_simple_prepend(self):
        self.singly_linked_list.prepend(1)

        self.assertEqual(self.singly_linked_list._head.data, 1)
        self.assertEqual(len(self.singly_linked_list), 1)
        self.assertEqual(self.singly_linked_list._tail.next, None)
        self.assertEqual(self.singly_linked_list._tail.data, 1)
    def test_multiple_prepends(self):
        self.singly_linked_list.prepend(1)
        self.singly_linked_list.prepend(2)
        self.singly_linked_list.prepend(3)

        self.assertEqual(self.singly_linked_list._head.data, 3)
        self.assertEqual(self.singly_linked_list._head.next.data, 2)
        self.assertEqual(self.singly_linked_list._tail.data, 1)
        self.assertEqual(len(self.singly_linked_list), 3)
        self.assertEqual(self.singly_linked_list._tail.next, None)


    def test_simple_insert(self):
        self.singly_linked_list.build_forward_from_list(self.test_list1) 

        self.singly_linked_list.insert_after(3, 69)
        self.assertEqual(self.singly_linked_list._head.next.next.next.data, 69)
        self.assertEqual(len(self.singly_linked_list), 5)
        self.assertEqual(self.singly_linked_list._tail.next, None)
        self.assertEqual(self.singly_linked_list._tail.data, 4)
    def test_tail_insert(self):
        self.singly_linked_list.build_forward_from_list(self.test_list1)

        self.singly_linked_list.insert_after(4, 69)
        self.assertEqual(self.singly_linked_list._tail.data, 69)
        self.assertEqual(len(self.singly_linked_list), 5)
        self.assertEqual(self.singly_linked_list._tail.next, None)
    def test_missing_insert(self):
        self.singly_linked_list.build_forward_from_list(self.test_list1) 

        with self.assertRaises(ValueError):
            self.singly_linked_list.insert_after(70, 69)
        self.assertEqual(self.singly_linked_list._tail.next, None)
        self.assertEqual(self.singly_linked_list._tail.data, 4)


    def test_simple_remove(self):
        self.singly_linked_list.build_forward_from_list(self.test_list1)

        self.singly_linked_list.remove(3)
        self.assertEqual(self.singly_linked_list._head.next.next.data, 4)
        self.assertEqual(len(self.singly_linked_list), 3)
        self.assertEqual(self.singly_linked_list._tail.next, None)
        self.assertEqual(self.singly_linked_list._tail.data, 4)
    def test_tail_remove(self):
        self.singly_linked_list.build_forward_from_list(self.test_list1)

        self.singly_linked_list.remove(4)
        self.assertEqual(self.singly_linked_list._head.next.next.next, None)
        self.assertEqual(len(self.singly_linked_list), 3)
        self.assertEqual(self.singly_linked_list._tail.next, None)
        self.assertEqual(self.singly_linked_list._tail.data, 3)
    def test_head_remove(self):
        self.singly_linked_list.build_forward_from_list(self.test_list1)

        self.singly_linked_list.remove(1)
        self.assertEqual(self.singly_linked_list._head.data, 2)
        self.assertEqual(len(self.singly_linked_list), 3)
        self.assertEqual(self.singly_linked_list._tail.next, None)
        self.assertEqual(self.singly_linked_list._tail.data, 4)
    def test_final_remove(self):
        self.singly_linked_list.append(1)

        self.singly_linked_list.remove(1)
        self.assertEqual(self.singly_linked_list._head, None)
        self.assertEqual(len(self.singly_linked_list), 0)
    def test_missing_remove(self):
        self.singly_linked_list.append(1)

        with self.assertRaises(ValueError):
            self.singly_linked_list.remove(6)
        self.assertEqual(self.singly_linked_list._tail.next, None)
        self.assertEqual(self.singly_linked_list._tail.data, 1)


    def test_list_contains(self):
        self.singly_linked_list.append(1)

        self.assertTrue(self.singly_linked_list.contains(1))
        self.assertFalse(self.singly_linked_list.contains(2))
        self.assertEqual(self.singly_linked_list._tail.next, None)
        self.assertEqual(self.singly_linked_list._tail.data, 1)


    def test_empty_list(self):
        self.assertTrue(self.singly_linked_list.is_empty())
        self.singly_linked_list.append(1)
        self.assertFalse(self.singly_linked_list.is_empty())
        self.assertEqual(self.singly_linked_list._tail.next, None)
        self.assertEqual(self.singly_linked_list._tail.data, 1)


    def test_iterable(self):
        self.singly_linked_list.build_forward_from_list(self.test_list1)

        values = [value for value in self.singly_linked_list]
        self.assertEqual(values, [1, 2, 3, 4])

        
    def test_forward_build(self):
        test_list = [1, 2, 3, 4, 5]
        self.singly_linked_list.build_forward_from_list(test_list)    
        iterated_list = [value for value in self.singly_linked_list]
        self.assertEqual(self.singly_linked_list._tail.next, None)
        self.assertEqual(self.singly_linked_list._tail.data, 5)

        self.assertEqual(len(self.singly_linked_list), 5)
        self.assertEqual(test_list, iterated_list)
    def test_backward_build(self):
        test_list = [1, 2, 3, 4, 5]
        self.singly_linked_list.build_backward_from_list(test_list)    
        iterated_list = [value for value in self.singly_linked_list]

        self.assertEqual(len(self.singly_linked_list), 5)
        self.assertEqual([5,4,3,2,1], iterated_list)
        self.assertEqual([1, 2, 3, 4, 5], test_list)
        self.assertEqual(self.singly_linked_list._tail.next, None)
        self.assertEqual(self.singly_linked_list._tail.data, 1)


    def test_remove_all(self):
        self.singly_linked_list.build_forward_from_list(self.test_list2)

        self.singly_linked_list.remove_all_target(3)

        self.assertEqual(len(self.singly_linked_list), 3)
        self.assertFalse(self.singly_linked_list.contains(3))
        self.assertEqual(self.singly_linked_list._tail.next, None)
        self.assertEqual(self.singly_linked_list._tail.data, 4)
    def test_remove_all_target_count(self):
        self.singly_linked_list.build_forward_from_list(self.test_list2)

        self.assertEqual(self.singly_linked_list.remove_all_target(3), 4)
        self.assertEqual(self.singly_linked_list._tail.next, None)
        self.assertEqual(self.singly_linked_list._tail.data, 4)
    def test_remove_all_missing_target(self):
        self.singly_linked_list.build_forward_from_list(self.test_list2)

        self.assertEqual(self.singly_linked_list.remove_all_target(53), 0)
        self.assertEqual(self.singly_linked_list._tail.next, None)
        self.assertEqual(self.singly_linked_list._tail.data, 3)

    
    def test_str_method(self):
        self.singly_linked_list.build_forward_from_list(self.test_list1)

        self.assertEqual(str(self.singly_linked_list), "Head>  1 -> 2 -> 3 -> 4  <Tail")
    def test_str_method_single(self):
        self.singly_linked_list.append(1)

        self.assertEqual(str(self.singly_linked_list), "Head>  1  <Tail")
    def test_str_method_zero(self):
        self.assertEqual(str(self.singly_linked_list), "Head>    <Tail")

if __name__ == "__main__":
    unittest.main()