class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.length = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index >= self.length:
            return -1
        cur = self.head
        for i in range(index):
            cur = cur.next
        return cur.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        n = Node(val)
        n.next = self.head
        self.head = n
        self.length += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        n = Node(val)
        if not self.length:
            self.head = n
            self.length = 1
            return

        cur = self.head
        for i in range(self.length - 1):
            cur = cur.next
        cur.next = n
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index > self.length:
            return
        if index == self.length:
            return self.addAtTail(val)

        n = Node(val)
        if index == 0:
            return self.addAtHead(val)

        cur = self.head
        for i in range(index - 1):
            cur = cur.next
        n.next = cur.next
        cur.next = n
        self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index >= self.length:
            return
        if index == 0:
            self.head = self.head.next
            self.length -= 1
            return
        cur = self.head
        for i in range(index - 1):
            cur = cur.next
        cur.next = cur.next.next
        self.length -= 1
