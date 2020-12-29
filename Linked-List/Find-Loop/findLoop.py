# Time Complexity = O(n), because first pointer will traverse exactly all the nodes | Space Complexity = O(1)

class LinkedList:
    def __init__(self, value):
        self.value = value 
        self.next = None

def findLoop(head):
    # set 2 pointers at the second index and the third index, to avoid immediately clashing
    first = head.next
    second = head.next.next
    while first != second:
        first = first.next
        second = second.next.next
    first = head
    while first != second:
        first = first.next
        second = second.next
    return first  