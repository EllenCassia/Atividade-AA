def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        if n % 2 == 0:
            k = n // 2
            return (fibonacci(k) * (2 * fibonacci(k + 1) - fibonacci(k)))
        else:
            k = (n + 1) // 2
            return (fibonacci(k) ** 2 + fibonacci(k - 1) ** 2)

fib = [0] * 110
fib[1] = 1
fib[2] = 2

for i in range(3, 46):
    fib[i] = fibonacci(i)

print("n: ")
n = int(input())

for _ in range(n):

    print("quilometros: ")
    m = int(input())
    i = 45
    ans = 0
    while i > 1:
        if fib[i] <= m:
            m -= fib[i]
            ans += fib[i - 1]
        i -= 1
    print("milhas: ")
    print(ans)
