# Time Complexity = O(n), because first node is  | Space Complexity = O(1) 

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def removeKthNodeFromEnd(head, k):
    first, second = head, head
    position = 1
    while position <= k:
        second = second.next
        position += 1
    # Need to handle edge case here, if second has already reached the end
    if second is None:
        head.value = head.next.value
        head.next = head.next.next
        return
    while second.next != None:
        first = first.next
        second = second.next
    first.next = first.next.next

    # cannot do second != None and do first.prev.next = first.next, because 
    # singly linked list, there is no prev!

