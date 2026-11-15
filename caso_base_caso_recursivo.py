def regressiva(i):
    print(i)
    if i <= 1:
        print("Fim do programa")
    else:
        regressiva(i-1)

regressiva(3)
