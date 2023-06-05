print("tam: ")
tam = int(input())
print("q: ")
q = list(map(int, input().split()))
print("n: ")
n = list(map(int, input().split()))

quant = 0
for i in range(len(n)):
    j = 0
    aux = 0
    while j < len(q) and len(q) != 0:
        if(n[i] > q[j]):
            q.remove(q[j])
            j=0
            aux += 1
        else:
            j+=1

    if(aux >= quant):
        quant = aux
    
print(quant)
