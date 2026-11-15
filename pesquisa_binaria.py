def pesquisa_binaria(arr: list, item: int) -> int:
    baixo = 0
    alto = len(arr) - 1

    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = arr[meio]
        if chute == item:
            return meio
        elif chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1
    return None

minha_lista = [1,3,5,7,9]

print(pesquisa_binaria(minha_lista, 3))
print(pesquisa_binaria(minha_lista, -1))

