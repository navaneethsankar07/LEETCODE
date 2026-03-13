class Node:
    def __init__(self,val):
        self.val = val
        self.prev = None
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        curr = self.head
        count = 0
        while curr and count < index:
            curr = curr.next
            count += 1
        if curr is None:
            return -1 

        return curr.val

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)

        if self.head:
            self.head.prev = new_node
            new_node.next = self.head
        
        self.head = new_node

    def addAtTail(self, val: int) -> None:
        curr = self.head
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
            return
            
        while curr.next:
            curr = curr.next
        
        curr.next = new_node
        new_node.prev = curr

    def addAtIndex(self, index: int, val: int) -> None:
        new_node = Node(val)

        if index == 0:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
            return
        
        curr = self.head
        count = 0
        while curr and count < index-1:
            curr = curr.next
            count += 1
        
        if curr is None:
            return

        new_node.next = curr.next
        new_node.prev = curr

        if curr.next:
            curr.next.prev = new_node
        
        curr.next = new_node

    def deleteAtIndex(self, index: int) -> None:

        if self.head is None:
            return
        
        curr = self.head
        count = 0

        while curr and count < index:
            curr = curr.next
            count += 1

        if curr is None:
            return
        
        if curr.prev is None:
            self.head = curr.next
            if self.head:
                self.head.prev = None
            return
        
        curr.prev.next = curr.next

        if curr.next:
            curr.next.prev = curr.prev

