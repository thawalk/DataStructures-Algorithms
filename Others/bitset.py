# a & b AND
# a | b OR
# a ^ b XOR
# ~a NOT
# 

a = -3
b = 1

class BitSet:
    def __init__(self):
        pass
    
    def AND(self, valueA, valueB):
        return (valueA & valueB)

    def OR(self, valueA, valueB):
        return (valueA | valueB)

    def XOR(self, valueA, valueB):
        return (valueA ^ valueB)

    def NOT(self, valueA):
        return (~valueA)

    def leftShift(self, valueA, n):
        return (valueA << n)

    def rightShift(self, valueA, n):
        return (valueA >> n)


bitset = BitSet()
print(bitset.NOT(a))




print(a & b)