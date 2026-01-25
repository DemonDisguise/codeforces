def find_lexi(s, t):
    for i in range(len(s)):
        if s[i] < t[i]:
            return -1
        elif s[i] > t[i]:
            return 1
    return 0

if __name__ == "__main__":
    s = input().lower()
    t = input().lower()
    print(find_lexi(s, t))
        