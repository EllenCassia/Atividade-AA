fib = [0] * 110
fib[1] = 1
fib[2] = 2

for i in range(3, 46):
    fib[i] = fib[i - 1] + fib[i - 2]

print("n: ")
n = int(input())

for _ in range(n):
    print("m: ")
    m = int(input())
    i = 45
    ans = 0
    while i > 1:

        if fib[i] <= m:
            m -= fib[i]
            ans += fib[i - 1]
        i -= 1
    print(ans)
