
tam = int(input())
q = list(map(int, input().split()))
n = list (map(int, input().split()))
q.sort()
n.sort()
n.reverse()

aux = tam
indice = -1
quantidade = 0
inicio = 0
fim = tam - 1
continuar = True

while (continuar and indice < tam and fim > -1):
    inicio = 0
    fim = aux - 1
    indice += 1
    aux = -1

    while (inicio <= fim):
        meio = (inicio + fim) // 2
        if (n[indice] <= q[meio] and inicio != fim):
           fim = meio - 1
           continue
        elif (n[indice] > q[meio] and inicio != fim):
           inicio = meio + 1
           aux = meio
           continue
        elif (n[indice] > q[meio] and inicio == fim):
           inicio = 0
           fim = meio - 1
           indice += 1
           quantidade += 1
           aux = -1
           continue
        elif(aux == -1):
            continuar = False
            break

        break

print(quantidade)