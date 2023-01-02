# This program consists of the basic operations of a linked list: 
# 1. Create a linked list
# 2. Add a node at beginning
# 3. Add a node at end
# 4. Add a node at given index
# 5. Get length of linked list
# 6. Delete linked list

from node import Node

class LinkedList:
    def __init__(self):
        self.head = None

    # Function to insert a node at the beginning (at head) of the linked list
    def insertAtBeginning(self, data):
        node = Node(data, self.head)
        self.head = node

    # Function to insert a node at the end of the linked list
    def insertAtEnd(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            itr = self.head
            while itr.next:
                itr=itr.next
            itr.next = Node(data)
    
    # Function to insert a node at a given index of the linked list
    def insertAt(self, data, index):
        if index<0 or index>=self.ListLength()+1:
            raise Exception("Invalid index")
        
        count=0
        itr=self.head
        while count<index-1:
            count+=1
            itr=itr.next

        node = Node(data)
        node.next = itr.next
        itr.next=node
    
    # Function to find the length of the linked list
    def listLength(self):
        count=0
        itr=self.head
        while itr:
            count+=1
            itr=itr.next
        return count

    # Function to delete the entire linked list
    def deleteList(self):
        self.head = None # This will remove all references to the nodes in the linked list, 
                         # allowing them to be garbage collected

    # Function to delete a node at a given index of the linked list
    def deleteAt(self, index):
        if index<0 or index>=self.ListLength():
            raise Exception("Invalid Index")
        
        if index==0:
            self.head=self.head.next

        count=0
        itr=self.head
        while count<index-1:
            count+=1
            itr=itr.next

        itr.next=itr.next.next

    # Find the index of a the given value
    def findIndex(self,data):
        pass

    # Function to insert a node at the beginning (at head) of the linked list
    def printList(self):
        pass

    