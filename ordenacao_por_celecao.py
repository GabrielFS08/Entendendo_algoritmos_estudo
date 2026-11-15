def busca_Menor(arr):
    menor = arr[0]
    menor_indice = 0
    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_indice = i
    return menor_indice


def ordenacao_por_Selecao(arr):
    novoArr = []
    copiaArr = list(arr)
    for i in range(len(copiaArr)):
        menor = busca_Menor(copiaArr)
        novoArr.append(copiaArr.pop(menor))
    return novoArr

print(ordenacao_por_Selecao([5, 3, 6, 2, 10]))
