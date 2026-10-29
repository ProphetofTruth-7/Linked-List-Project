import unittest
from evens_and_odds_subclass import EvensAndOdds

class TestEvensAndOdds(unittest.TestCase):
    def setUp(self):
        self.evens_and_odds_list = EvensAndOdds()
        self.test_list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 15]
        self.test_list4 = [86, 45, 34, 78, 79, 34, 20, 39, 4, 32, 11]
        self.test_list5 = [2, 6, 8, 10]
        self.test_list6 = [3, 7, 9, 11]
        self.test_list7 = [3, 2, 9, 11]
        self.test_list8 = [2, 7, 8, 10]
        self.test_list9 = []

    def test_ordered_splitter(self):
        self.evens_and_odds_list.build_forward_from_list(self.test_list3)
        even_list, odd_list = self.evens_and_odds_list.split_even_odd()

        self.assertEqual(len(self.evens_and_odds_list), 0)
        self.assertEqual(self.evens_and_odds_list._head, None)
        self.assertEqual(self.evens_and_odds_list._tail, None)

        self.assertEqual(len(even_list), 5)
        self.assertEqual(len(odd_list), 8)
        self.assertEqual(str(even_list), "Head>  2 -> 4 -> 6 -> 8 -> 10  <Tail")
        self.assertEqual(str(odd_list), "Head>  1 -> 3 -> 5 -> 7 -> 9 -> 11 -> 13 -> 15  <Tail")

        self.assertEqual(even_list._tail.next, None)
        self.assertEqual(even_list._tail.data, 10)
        self.assertEqual(odd_list._tail.next, None)
        self.assertEqual(odd_list._tail.data, 15)
        self.assertEqual(len(self.evens_and_odds_list), 0)

    def test_unordered_splitter(self):
        self.evens_and_odds_list.build_forward_from_list(self.test_list4)
        even_list, odd_list = self.evens_and_odds_list.split_even_odd()

        self.assertEqual(len(self.evens_and_odds_list), 0)
        self.assertEqual(self.evens_and_odds_list._head, None)
        self.assertEqual(self.evens_and_odds_list._tail, None)

        self.assertEqual(len(even_list), 7)
        self.assertEqual(len(odd_list), 4)
        self.assertEqual(str(even_list), "Head>  86 -> 34 -> 78 -> 34 -> 20 -> 4 -> 32  <Tail")
        self.assertEqual(str(odd_list), "Head>  45 -> 79 -> 39 -> 11  <Tail")

        self.assertEqual(even_list._tail.next, None)
        self.assertEqual(even_list._tail.data, 32)
        self.assertEqual(odd_list._tail.next, None)
        self.assertEqual(odd_list._tail.data, 11)
        self.assertEqual(len(self.evens_and_odds_list), 0)

    def test_even_splitter(self):
        self.evens_and_odds_list.build_forward_from_list(self.test_list5)
        even_list, odd_list = self.evens_and_odds_list.split_even_odd()

        self.assertEqual(len(self.evens_and_odds_list), 0)
        self.assertEqual(self.evens_and_odds_list._head, None)
        self.assertEqual(self.evens_and_odds_list._tail, None)

        self.assertEqual(len(even_list), 4)
        self.assertEqual(len(odd_list), 0)
        self.assertEqual(str(even_list), "Head>  2 -> 6 -> 8 -> 10  <Tail")
        self.assertEqual(str(odd_list), "Head>    <Tail")

        self.assertEqual(even_list._tail.next, None)
        self.assertEqual(even_list._tail.data, 10)
        self.assertEqual(odd_list._tail, None)
        self.assertEqual(len(self.evens_and_odds_list), 0)

    def test_odd_splitter(self):
        self.evens_and_odds_list.build_forward_from_list(self.test_list6)
        even_list, odd_list = self.evens_and_odds_list.split_even_odd()

        self.assertEqual(len(self.evens_and_odds_list), 0)
        self.assertEqual(self.evens_and_odds_list._head, None)
        self.assertEqual(self.evens_and_odds_list._tail, None)

        self.assertEqual(len(even_list), 0)
        self.assertEqual(len(odd_list), 4)
        self.assertEqual(str(even_list), "Head>    <Tail")
        self.assertEqual(str(odd_list), "Head>  3 -> 7 -> 9 -> 11  <Tail")

        self.assertEqual(even_list._tail, None)
        self.assertEqual(odd_list._tail.next, None)
        self.assertEqual(odd_list._tail.data, 11 )
        self.assertEqual(len(self.evens_and_odds_list), 0)

    def test_single_even_splitter(self):
        self.evens_and_odds_list.build_forward_from_list(self.test_list7)
        even_list, odd_list = self.evens_and_odds_list.split_even_odd()

        self.assertEqual(len(self.evens_and_odds_list), 0)
        self.assertEqual(self.evens_and_odds_list._head, None)
        self.assertEqual(self.evens_and_odds_list._tail, None)

        self.assertEqual(len(even_list), 1)
        self.assertEqual(len(odd_list), 3)
        self.assertEqual(str(even_list), "Head>  2  <Tail")
        self.assertEqual(str(odd_list), "Head>  3 -> 9 -> 11  <Tail")

        self.assertEqual(even_list._tail.next, None)
        self.assertEqual(even_list._tail.data, 2)
        self.assertEqual(odd_list._tail.next, None)
        self.assertEqual(odd_list._tail.data, 11)
        self.assertEqual(len(self.evens_and_odds_list), 0)

    def test_single_odd_splitter(self):
        self.evens_and_odds_list.build_forward_from_list(self.test_list8)
        even_list, odd_list = self.evens_and_odds_list.split_even_odd()

        self.assertEqual(len(self.evens_and_odds_list), 0)
        self.assertEqual(self.evens_and_odds_list._head, None)
        self.assertEqual(self.evens_and_odds_list._tail, None)

        self.assertEqual(len(even_list), 3)
        self.assertEqual(len(odd_list), 1)
        self.assertEqual(str(even_list), "Head>  2 -> 8 -> 10  <Tail")
        self.assertEqual(str(odd_list), "Head>  7  <Tail")

        self.assertEqual(even_list._tail.next, None)
        self.assertEqual(even_list._tail.data, 10)
        self.assertEqual(odd_list._tail.next, None)
        self.assertEqual(odd_list._tail.data, 7)
        self.assertEqual(len(self.evens_and_odds_list), 0)


    def test_empty_list_splitter(self):
        self.evens_and_odds_list.build_forward_from_list(self.test_list9)

        with self.assertRaises(ValueError):
            even_list, odd_list = self.evens_and_odds_list.split_even_odd()


if __name__ == "__main__":
    unittest.main()