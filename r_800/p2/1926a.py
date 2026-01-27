from collections import Counter

for _ in range(int(input())):
    s = input()

    print(Counter(s).most_common(1)[0][0])
    