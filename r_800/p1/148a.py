import math
from itertools import combinations

# Input
numbers = [int(input()) for _ in range(4)]
d = int(input())

def count_divisible(nums, d):
    total = 0
    n = len(nums)
    
    for r in range(1, n + 1):
        for combo in combinations(nums, r):
            l = math.lcm(*combo)
            print(l)
            if r % 2 == 1:  
                total += d // l
            else:           
                total -= d // l
    return total

print(count_divisible(numbers, d))
