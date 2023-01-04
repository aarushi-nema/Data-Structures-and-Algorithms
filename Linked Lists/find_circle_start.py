from basic_operations import LinkedList

def find_loop(linkedlist: LinkedList):
        hare, tortoise = linkedlist.head, linkedlist.head
        while hare is not None and hare.next is not None:
            tortoise = tortoise.next
            hare = hare.next.next
        if hare == tortoise:
            return hare.data
        assert(False)