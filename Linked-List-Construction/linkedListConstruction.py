class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Time Complexity = O(1) | Space Complexity = O(1)
    def setHead(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return 
        self.insertBefore(self.head, node)
    
    # Time Complexity = O(1) | Space Complexity = O(1)
    def setTail(self, node):
        if self.tail is None:
            self.head = node
            self.tail = node
            return
        self.insertAfter(self.tail, node)

    # Time Complexity = O(1) | Space Complexity = O(1)
    def insertBefore(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        self.remove(nodeToInsert)
        nodeToInsert.prev = node.prev
        nodeToInsert.next = node
        if node.prev is None:
            self.head = nodeToInsert
        else:
            node.prev.next = nodeToInsert
        node.prev = nodeToInsert

    # Time Complexity = O(1) | Space Complexity = O(1)
    def insertAfter(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        self.remove(nodeToInsert)
        nodeToInsert.prev = node
        nodeToInsert.next = node.next
        if node.next is None:
            self.tail = nodeToInsert
        else:
            node.next.prev = nodeToInsert
        node.next = nodeToInsert

    # Time Complexity = O(p), where p is the position to insert at | Space Complexity = O(1)
    def insertAtPosition(self, position, nodeToInsert):
        if position == 1:
            self.setHead(nodeToInsert)
            return
        currentNode = self.head
        currentPosition = 1
        while currentNode is not None and currentPosition != position:
            currentNode = currentNode.next
            currentPosition += 1
        if currentNode is not None:
            self.insertBefore(currentNode, nodeToInsert)
        else:
            self.setTail(nodeToInsert)

    # Time Complexity = O(n) | Space Complexity = O(1)
    def removeNodesWithValue(self, value):
        currentNode = self.head
        while currentNode is not None:
            nodeToRemove = currentNode
            currentNode = currentNode.next
            if nodeToRemove.value == value:
                self.remove(nodeToRemove)



    # Time Complexity = O(1) | Space Complexity = O(1)
    def remove(self, node):
        if node == self.head:
            self.head = self.head.next
        if node == self.tail:
            self.tail = self.tail.prev
        self.removeNodeBindings(node)

    # Time Complexity = O(n) | Space Complexity = O(1)
    def containsNodeWithValue(self, value):
        currentNode = self.head
        while currentNode is not None and currentNode.value != value:
            currentNode = currentNode.next
        return currentNode is not None

    def removeNodeBindings(self, node):
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        node.prev = None
        node.next = None