def pesquisa(arr, item):
	baixo = 0
	alto = len(arr) - 1
	while alto >= baixo:
		meio = (baixo + alto) // 2
		chute = arr[meio]
		if chute == item:
			return meio
		elif chute > item:
			alto = meio - 1
		else:
			baixo = meio + 1

print(pesquisa([12, 34, 56, 78, 12, 89], 34))
