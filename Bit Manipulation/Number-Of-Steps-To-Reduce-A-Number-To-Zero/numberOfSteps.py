# Time Complexity = O(logn) | Space Complexity = O(1)

# def numberOfSteps (num):
#     steps = 0
#     while num:
#         steps += 1
#         if num % 2 == 0:
#             num /= 2
#         else:
#             num -= 1
#     return steps

# Time Complexity = O(logn) | Space Complexity = O(1)

# def numberOfSteps (self, num):
    
#     steps = 0

#     # Get the binary for num, as a String. Remove the "0b" off the start with splice.
#     binary = bin(num)[2:]
    
#     # Iterate over all the bits in the binary string.
#     for bit in binary:
#         # Must use "1", not 1 here. The bits are strings!
#         if bit == "1": # If the bit is a 1 
#             steps = steps + 2 # Then it'll take 2 to remove.
#         else: # bit == "0"
#             steps = steps + 1 # Then it'll take 1 to remove.

#     # We need to subtract 1, because the last bit was over-counted.
#     return steps - 1

# Time Complexity = O(logn) | Space Complexity = O(1)

def numberOfSteps (self, num):

    # We need to handle this as a special case, otherwise it'll return -1.
    if num == 0: return 0
    
    steps = 0
    power_of_two = 1
    
    while power_of_two <= num:
        # Apply the bit mask to check if the bit at "power_of_two" is a 1.
        if (power_of_two & num) != 0:
            steps = steps + 2
        else:
            steps = steps + 1
        power_of_two = power_of_two * 2
    
    # We need to subtract 1, because the last bit was over-counted.
    return steps - 1