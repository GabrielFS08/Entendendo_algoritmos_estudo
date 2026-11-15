def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivo = array[0] # pivo = 1
        menores = [i for i in array[1:] if i <= pivo] # menores = []
        maiores = [i for i in array[1:] if i > pivo] # maiores = [9,6,2,8]
        return quicksort(menores) + [pivo] + quicksort(maiores)

''' quicksort([]) + [1] + quicksort([9, 6, 2, 8]) = [] + [1] + [2, 6, 8, 9] = [1, 2, 6, 8, 9]

    quicksort([6, 2, 8]) + [9] + quicksort([]) = [2, 6, 8] + [9] + []

    quicksort([2]) + [6] + quicksort([8]) =  [2] + [6] + [8]'''


print(f"Essa é a lista ordenada {quicksort([1,9,6,2,8])}")
