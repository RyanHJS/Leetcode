# Counting Bits

# Given an integer num, return an array of the number of 1's in the binary representation of every number in the range [0, num].
# 0     0       0
# 1	    1       1
# 2	    10      1
# 3	    11      2
# 4	    100     1
# 5	    101     2
# 6	    110     2
# 7	    111     3
# 8	    1000    1
# 9	    1001    2
# 10	1010    2

def countBits(num: int):

    ans = [0]
    for i in range(1, num+1):
        ans.append(ans[i//2] + i % 2)
    return ans

print(countBits(5))