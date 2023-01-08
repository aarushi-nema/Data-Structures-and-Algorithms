#This program finds the nth node of the linked list form the beginning

from basic_operations import LinkedList

def find_nth_node(linkedlist: LinkedList, n):
    itr = linkedlist.head
    count = 0
    while itr:
        if count == n:
            return itr.data
        count += 1
        itr=itr.next

    assert(False)
       