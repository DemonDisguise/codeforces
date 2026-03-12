from collections import Counter

for _ in range(int(input())):
    input()
    a, b = input().split()

    freq = [0] * 26
    
    for i in range(len(a)):
        freq[ord(a[i]) - ord('a')] += 1
        freq[ord(b[i]) - ord('a')] -= 1
        
    print("YES" if all(x == 0 for x in freq) else "NO")