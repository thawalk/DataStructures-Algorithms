import reverseLinkedList
import unittest


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

    def addMany(self, values):
        current = self
        while current.next is not None:
            current = current.next
        for value in values:
            current.next = LinkedList(value)
            current = current.next
        return self

    def getNodesInArray(self):
        nodes = []
        current = self
        while current is not None:
            nodes.append(current.value)
            current = current.next
        return nodes


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        test = LinkedList(0).addMany([1, 2, 3, 4, 5])
        result = reverseLinkedList.reverseLinkedList(test).getNodesInArray()
        expected = LinkedList(5).addMany([4, 3, 2, 1, 0]).getNodesInArray()
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()