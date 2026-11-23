def menor_indice(arr):
    menor = arr[0]
    menor_indice = 0
    for i in range(len(arr)):
        if menor > arr[i]:
            menor = arr[i]
            menor_indice = i
    return menor_indice

def ordenacao(arr):
    novo_arr = []
    copia_arr = list(arr)
    for i in range(len(copia_arr)):
        menor = menor_indice(copia_arr)
        novo_arr.append(copia_arr.pop(menor))
    return novo_arr

print(ordenacao([2,4,1,5,6,8,12,11]))
