# Função recursiva que calcula o fatorial


def calcFat(num):
    # Caso-base
    # Se o número for = 0 ou = 1, o resultado
    # que vai ser retornado, será 1
    if (num == 0) or (num == 1):
        return 1

    # Caso recursivo
    # O resultado que vai ser retornado, será
    # o valor do número multiplicado pelo fatorial dele -1
    else:
        return num * calcFat(num-1)


x = int(input("Informe um número: "))
result = calcFat(x)
print("O fatorial de {} é {} ".format(x, result))
