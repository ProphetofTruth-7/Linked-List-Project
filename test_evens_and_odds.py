import unittest
from evens_and_odds_subclass import EvensAndOdds

class TestEvensAndOdds(unittest.TestCase):
    def setUp(self):
        self.evens_and_odds_list = EvensAndOdds()
        self.test_list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 15]
        self.test_list4 = [86, 45, 34, 78, 79, 34, 20, 39, 4, 32, 11]

    def test_ordered_splitter(self):
        self.evens_and_odds_list.build_forward_from_list(self.test_list3)
        even_list, odd_list = self.evens_and_odds_list.split_even_odd()

        self.assertEqual(len(self.evens_and_odds_list), 0)
        self.assertEqual(len(even_list), 5)
        self.assertEqual(len(odd_list), 8)
        self.assertEqual(str(even_list), "Head>  2 -> 4 -> 6 -> 8 -> 10  <Tail")
        self.assertEqual(str(odd_list), "Head>  1 -> 3 -> 5 -> 7 -> 9 -> 11 -> 13 -> 15  <Tail")

    def test_unordered_splitter(self):
        self.evens_and_odds_list.build_forward_from_list(self.test_list4)
        even_list, odd_list = self.evens_and_odds_list.split_even_odd()

        self.assertEqual(len(self.evens_and_odds_list), 0)
        self.assertEqual(len(even_list), 7)
        self.assertEqual(len(odd_list), 4)
        self.assertEqual(str(even_list), "Head>  86 -> 34 -> 78 -> 34 -> 20 -> 4 -> 32  <Tail")
        self.assertEqual(str(odd_list), "Head>  45 -> 79 -> 39 -> 11  <Tail")


if __name__ == "__main__":
    unittest.main()