from evens_and_odds_subclass import EvensAndOdds
from singly_linked_list import SinglyLinkedList


linked_list_object = SinglyLinkedList()
linked_list_object2 = SinglyLinkedList()
showcase_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print("Welcome to the Linked List Showcase!")
print()

linked_list_object.build_forward_from_list(showcase_list)
print(f"Collated Linked List:   {linked_list_object}") 
linked_list_object2.build_backward_from_list(showcase_list)
print(f"Collated Linked List(but backwards):   {linked_list_object2}") 
linked_list_object.insert_after(8, 5)
print(f"With the Forward List, we can add a 5 after the 8 to get:   {linked_list_object}")
linked_list_object.remove(6)
print(f"Then, we can remove the 6 to get:   {linked_list_object}")
linked_list_object.remove_all_target(5)
print(f"Then, we can remove all the 5's to get:   {linked_list_object}")

evens_and_odds_object = EvensAndOdds()
showcase2_list = [1, 2, 3, 4, 7, 8, 9]
evens_and_odds_object.build_forward_from_list(linked_list_object)
even_list, odd_list = evens_and_odds_object.split_even_odd()
print(f"With the EvensAndOdds subclass, we can split the list {linked_list_object} via even/odd: ")
print(f"         Even list: {even_list}")
print(f"         Odd list: {odd_list}")
print(f"Leaving an empty list: {evens_and_odds_object}")
even_list.remove(2)
print(f"Normal method still work, say...removing 2 from the even list: {even_list}")
print(f"Removing a 3 from even returns a ValueError, as expected. Go ahead! Try it...")