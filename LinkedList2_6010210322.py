"""Linked List lab 2
Incomplete implementation of a list ADT using a singly linked list."""
class SinglyLinkedList(object):
    """Singly Linked List Class"""

    class Node(object):
        """A nested storage class representing list nodes."""
        def __init__(self,item, next=None):
            """Instantiaties a Node with default next of Node"""
            self.data = item
            self.next = next

    def __init__(self):
        """Constructs an empty list"""
        self._head = None

    def insertBegin(self, item):
        """Adds a new item to the beginning (head) of the list."""

        if self._head is None:
            self._head = SinglyLinkedList.Node(item)
        else:
            newNode = SinglyLinkedList.Node(item)
            newNode.next = self._head
            self._head = newNode

    def visitNode(self):
        curNode = self._head
        while curNode is not None:
            print curNode.data,
            curNode = curNode.next
#------------------------------------------------------
#Unfinished methods
#------------------------------------------------------
    def insert(self, index, item):
        """Adds a new item at index i."""
        if self._head is None or index <= 0 :
            self._head = SinglyLinkedList.Node(item)
        else:
            newNode = SinglyLinkedList.Node(item)
            curNode = self._head
            while index > 1 and curNode.next is not None:
                curNode = curNode.next
                index   = index-1
            newNode.next = curNode.next
            curNode.next = newNode


    def remove(self, target):
        """Removes an instance of the item from the list"""
        curNode  = self._head
        preNode = None

        while curNode is not None and curNode.data is not target:
            preNode = curNode
            curNode = curNode.next
        if curNode is not None:
            if curNode is self._head:
                head = curNode.next
            else:
                preNode.next = curNode.next


#------------------------------------------------------

def main():

    #Create a list using adding new item at the beginning of the list
    datalist = SinglyLinkedList()
    for i in xrange(1, 11):
        datalist.insertBegin(i)
    datalist.visitNode()

    #Insert a new item at index i
    print ("\nInsert item at specific position")
    # add your code here
    item = input("Enter a positon to insert: ")
    item1 = input("Enter a new data: ")
    datalist.insert(item,item1)
    datalist.visitNode()

    #---------------------------------------------------------

    #Remove item from the list
    print ("\nRemove item from the list")
    target = int(input("Enter a target number: "))
    # add your code here
    datalist.remove(target)
    datalist.visitNode()
    #---------------------------------------------------------


if __name__ == '__main__':
    main()