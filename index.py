# print("hello world")

# produto = "Hamburger"
# quantidade = 2
# preco = 29.90   
# esta_disponivel = True      
# valor_total = quantidade * preco

# print(f"Pedido: {quantidade}x {produto}")
# print(f"Total a pagar: R${valor_total:.2f}")

# # Dados do pedido
# produto = "Combo Família"
# preco_total = 125.50

# print(f"Processando pedido: {produto}")
# print(f"Valor original: R$ {preco_total}")

# # --- Lógica de Desconto ---
# if preco_total > 50.00 and preco_total <= 100.00:
#     desconto = preco_total * 0.10  # 10% de desconto
#     valor_final = preco_total - desconto
#     print("✅ Você ganhou 10% de desconto por comprar acima de R$ 50!")
# elif preco_total > 100.00:  
#     desconto = preco_total * 0.20  # 20% de desconto
#     valor_final = preco_total - desconto
#     print("🎉 Parabéns! Você ganhou 20% de desconto por comprar acima de R$ 100!")   
# else:
#     valor_final = preco_total
#     print("ℹ️ Adicione mais itens para ganhar um desconto na próxima!")


# print(f"Valor a pagar: R$ {valor_final:.2f}")


# numeros = [1, 2, 3, 4, 5, 10, 20, 30, 40, 50]       

# contador = 0
# media = 0

# for n in numeros:
#     if n > 10:
#         print(n)
#         contador += 1
#         media += n

# if contador > 0:
#     media /= contador
#     print(f"A média dos números maiores que 10 é: {media:.2f}")

# print(f"Quantidade de números maiores que 10: {contador}")

# Comentar a função 
# comentar de linha a linha
# numeros = [1, 2, 3, 4, 5, 10, 20, 30, 40, 50]

# def maior_que_10(lista):
#     return [n for n in lista if n > 10]

# def calcular_media(lista):
#     if not lista:
#         return 0
#     return sum(lista) / len(lista)

# numeros_filtrados = maior_que_10(numeros)
# media = calcular_media(numeros_filtrados)

# print(f"Números maiores que 10: {numeros_filtrados}")
# print(f"Média: {media:.2f}")
def maior_que_10(lista):
    return [n for n in lista if n > 10]

def calcular_media(lista):
    if not lista:
        return 0
    return sum(lista) / len(lista)


numeros = []
maior = None 
menor = None

while True:
    entrada_texto = input('Digite um número (0 para sair): ').strip()

    if not entrada_texto:
        print('Por favor, digite um valor.')
        continue
        
    try:
        entrada = int(entrada_texto)
    except ValueError:
        print('Entrada inválida. Digite um número inteiro.')
        continue

    if entrada == 0:
        break
    elif entrada < 0:
        print('Número negativo não é permitido.')
    else:
        numeros.append(entrada)

        if maior is None or entrada > maior:
            maior = entrada
        if menor is None or entrada < menor:
            menor = entrada

print(f'\nNúmeros digitados: {numeros}')

quantidade = len(numeros)

filtrados = sorted(maior_que_10(numeros), reverse=True)
media = calcular_media(filtrados)

print(f'Números maiores que 10: {filtrados}')
print(f'Quantidade de números: {quantidade}')
print(f'Média: {media:.2f}')

if numeros:
    print(f'Maior número digitado: {maior}')
    print(f'Menor número digitado: {menor}')
else:
    print("Nenhum número foi digitado.")