# Find runner-Up score
if __name__ == '__main__':
    n = int(input())
    arr = []
    for i in range(n):
        n = int(input())
        arr.append(n)
    arr.sort(reverse=True)
    s = set(arr)
    print(s[1])
