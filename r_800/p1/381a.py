n = int(input())
nums = list(map(int, input().split()))

l, r = 0, n - 1
x = y = 0
turn = 0  

while l <= r:
    if nums[l] >= nums[r]:
        val = nums[l]
        l += 1
    else:
        val = nums[r]
        r -= 1

    if turn == 0:
        x += val
    else:
        y += val

    turn ^= 1 

print(x, y)
