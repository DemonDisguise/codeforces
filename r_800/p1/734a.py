n = int(input())
s = input()

a_cnt = s.count('A')

if a_cnt > n - a_cnt:
    print("Anton")
elif a_cnt < n - a_cnt:
    print("Danik")
else:
    print("Friendship")