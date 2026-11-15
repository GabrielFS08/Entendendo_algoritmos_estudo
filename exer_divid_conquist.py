# questão 1:
def soma(lista):
    if lista == []:
        return 0
    return lista[0] + soma(lista[1:])

'''10 + soma([20, 30])
   10 + (20 + soma([30]))
   10 + (20 + (30 + soma([])))
   10 + (20 + (30 + 0)) = 60'''

print(f"O resultado da soma dos elementos é {soma([10,20,30])}")


# questão 2:
def contar(lista):
    if lista == []:
        return 0
    return 1 + contar(lista[1:])

'''1 + soma([20, 30])
   1 + (1 + soma([30]))
   1 + (1 + (1 + soma([])))
   1 + (1 + (1 + 0)) = 3'''

print(f"O número de elementos na lista é {contar([10,20,30])}")


# questão 3:
def max_value(lista):
    if len(lista) == 2:
        return lista[0] if lista[0] > lista[1] else lista[1]

    sub_max = max(lista[1:]) # sub_max = [20,30], max(sub_max) = 30
    return lista[0] if lista[0] > sub_max else sub_max # lista[0] = 10 não é maior do que sub_max, ELSE retorna o sub_max = 30

print(f"O maior número da lista é {max_value([10,20,30])}")

# questão 4:
''' O caso-base é quando a lista possui apenas um valor, se o valor buscado for igual a um elelmento do array, então ele foi e
ncontrado, caso ao contrário isso significa que o valor não está no array.
E no caso recursivo, a pesquisa binária divide o array ao meio, descarta uma das metades e chama a pesquisa binária na metade 
restante.'''
