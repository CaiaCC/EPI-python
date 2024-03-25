# count the number of bits
# time: O(n), n = the number of bits needed to represent the integer
def count_bits(x: int) -> int:
    num_bits = 0
    while x:
        # add 1 if the rightmost bit is 1, otherwise add 0
        num_bits += x & 1
        # bit shifts to the right by 1, effectively // by 2
        x >>= 1
    return num_bits

'''
while loop output:
    
1100 & 0001 -> 0
0110 & 0001 -> 0
0011 & 0001 -> 1
0001 & 0001 -> 1
0000 -> break while loop
'''

if __name__ == '__main__':
    print(count_bits(12))

'''
NOTE: bit-wise operators
<<
    x << y
    Returns x with the bits shifted to the left by y places (and new bits on the right-hand-side are zeros). This is the same as multiplying x by 2**y.
>>
    x >> y
    Returns x with the bits shifted to the right by y places. This is the same as //'ing x by 2**y.
&
    x & y
    Does a "bitwise and". Each bit of the output is 1 if the corresponding bit of x AND of y is 1, otherwise it's 0.
|
    x | y
    Does a "bitwise or". Each bit of the output is 0 if the corresponding bit of x AND of y is 0, otherwise it's 1.
~
    ~ x
    Returns the complement of x - the number you get by switching each 1 for a 0 and each 0 for a 1. This is the same as -x - 1.
^
    x ^ y
    Does a "bitwise exclusive or". Each bit of the output is the same as the corresponding bit in x if that bit in y is 0, and it's the complement of the bit in x if that bit in y is 1.
'''