def busca_binaria(lista, alvo):
    inicio, fim = 0, len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2  # Divide a lista no meio
        if lista[meio] == alvo:
            return f"Encontrei {alvo}!"
        elif lista[meio] < alvo:
            inicio = meio + 1  # Olha na metade da direita
        else:
            fim = meio - 1  # Olha na metade da esquerda

    return "Não encontrei"

numeros = [1, 3, 5, 7, 9, 11, 13, 15]
print(busca_binaria(numeros, 7))  # Saída: Encontrei 7!

# Cada busca reduz o problema pela metade, tornando a busca MUITO rápida!
