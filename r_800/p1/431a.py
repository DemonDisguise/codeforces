cal = list(map(int, input().split()))
s = input()

# Taking this as ord is cheaper than int conversion
print(sum(cal[ord(i) - ord('1')] for i in s))
