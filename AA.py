def fibonacci(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1

    # Caso base: n é par
    if n % 2 == 0:
        m = n // 2
        fm = fibonacci(m)
        return fm * (2 * fibonacci(m - 1) + fm)

    # Caso base: n é ímpar
    else:
        m = (n + 1) // 2
        fm1 = fibonacci(m - 1)
        fm2 = fibonacci(m)
        return fm1 ** 2 + fm2 ** 2


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
    print("milhas: " + ans)








