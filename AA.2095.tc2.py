print("tam: ")
tam = int(input())
print("q: ")
q = list(map(int, input().split()))
print("n: ")
n = list (map(int, input().split()))
q.sort()
n.sort()

quant = 0

for i in range(tam):
    aux = 0
    for j in range(tam):
        if(n[i] > q[j]):
            aux += 1

    if(aux >= quant):
        quant = aux

print(quant)