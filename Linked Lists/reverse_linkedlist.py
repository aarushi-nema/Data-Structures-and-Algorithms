# This program takes in a linked list and reverses it
# This is the iterative approach
# The technique used here is the two pointer method.


from basic_operations import LinkedList

def reverse_list(linkedlist: LinkedList):
        prev, curr = None, linkedlist.head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        linkedlist.head = prev