# This function finds the middle of the linked list
# Technique used: Floyd's Tortoise and Hare Algorithm:
# A "tortoise" pointer is increased by 1 in every iteration
# A "hare" pointer is increased by two in every iteration
# Return the "tortoise" pointer once the "hare" pointer reaches end of linked list

from basic_operations import LinkedList

def find_middle(linkedList: LinkedList):
        hare, tortoise = linkedList.head, linkedList.head
        while hare is not None and hare.next is not None:
            tortoise = tortoise.next 
            hare = hare.next.next

        return(tortoise.data)