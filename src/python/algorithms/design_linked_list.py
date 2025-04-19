"""
Design your implementation of the linked list. 
You can choose to use a singly or doubly linked list.
A node in a singly linked list should have two 
attributes: val and next. val is the value of the current node, 
and next is a pointer/reference to the next node.
If you want to use the doubly linked list, you will need one more 
attribute prev to indicate the previous node in the linked list. 
Assume all nodes in the linked list are 0-indexed.

Implement the MyLinkedList class:

MyLinkedList() Initializes the MyLinkedList object.
- int get(int index) Get the value of the indexth node in the linked list. 
If the index is invalid, return -1.
- void addAtHead(int val) Add a node of value val before the first element 
of the linked list. After the insertion, the new node will be the first 
node of the linked list.
- void addAtTail(int val) Append a node of value val as the last element 
of the linked list.
- void addAtIndex(int index, int val) Add a node of value val before the 
indexth node in the linked list. If index equals the length of the linked list, 
the node will be appended to the end of the linked list. 
If index is greater than the length, the node will not be inserted.
- void deleteAtIndex(int index) Delete the indexth node in the linked list, 
if the index is valid.
"""
class Node:
    """
    A node in a doubly linked list.
    
    Attributes
    ----------
    val : int
        The value of the node.
    next : Node
        A pointer to the next node in the linked list.
    prev : Node
        A pointer to the previous node in the linked list.
    """
    
    def __init__(self, val: int):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:
    """
    A doubly linked list implementation.
    
    Attributes
    ----------
    head : Node
        The head of the linked list.
    tail : Node
        The tail of the linked list.
    size : int
        The number of nodes in the linked list.
    """
    
    def __init__(self):
        """
        Initializes the MyLinkedList object.
        """
        self.head = None
        self.tail = None
        self.size = 0

        
    def get(self, index: int) -> int:
        """
        Get the value of the indexth node in the linked list.
        If the index is invalid, return -1.
        """
        if index < 0 or index >= self.size:
            return -1
        current = self.head
        for _ in range(index):
            current = current.next
        return current.val
    

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list.
        After the insertion, the new node will be the first node of the linked 
        list.
        """
        new_node = Node(val)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1
    
    
    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val as the last element of the linked list.
        """ 
        new_node = Node(val)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
    
    
    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the indexth node in the linked list.
        If index equals the length of the linked list, the node will be
        appended to the end of the linked list.
        If index is greater than the length, the node will not be inserted.
        """
        if index < 0 or index > self.size:
            return
        if index == 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        else:
            new_node = Node(val)
            current = self.head
            for _ in range(index):
                current = current.next
            new_node.prev = current.prev
            new_node.next = current
            current.prev.next = new_node
            current.prev = new_node
            self.size += 1  

    
    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the indexth node in the linked list, if the index is valid.
        """
        if index < 0 or index >= self.size:
            return
        if index == 0:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
        elif index == self.size - 1:
            self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None
            else:
                self.head = None
        else:
            current = self.head
            for _ in range(index):
                current = current.next
            current.prev.next = current.next
            current.next.prev = current.prev
        self.size -= 1

# EOF
