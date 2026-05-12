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
# def maior_que_10(lista):
#     return [n for n in lista if n > 10]

# def calcular_media(lista):
#     if not lista:
#         return 0
#     return sum(lista) / len(lista)


# numeros = []
# maior = None 
# menor = None

# while True:
#     entrada_texto = input('Digite um número (0 para sair): ').strip()

#     if not entrada_texto:
#         print('Por favor, digite um valor.')
#         continue
        
#     try:
#         entrada = int(entrada_texto)
#     except ValueError:
#         print('Entrada inválida. Digite um número inteiro.')
#         continue

#     if entrada == 0:
#         break
#     elif entrada < 0:
#         print('Número negativo não é permitido.')
#     else:
#         numeros.append(entrada)

#         if maior is None or entrada > maior:
#             maior = entrada
#         if menor is None or entrada < menor:
#             menor = entrada

# print(f'\nNúmeros digitados: {numeros}')

# quantidade = len(numeros)

# filtrados = sorted(maior_que_10(numeros), reverse=True)
# media = calcular_media(filtrados)

# print(f'Números maiores que 10: {filtrados}')
# print(f'Quantidade de números: {quantidade}')
# print(f'Média: {media:.2f}')

# if numeros:
#     print(f'Maior número digitado: {maior}')
#     print(f'Menor número digitado: {menor}')
# else:
#     print("Nenhum número foi digitado.")
    
# numeros = []        
# while True:
#     print("\n--- MENU ---")
#     print("1 - Adicionar número")
#     print("2 - Ver números")
#     print("3 - Ver estatísticas")
#     print("4 - Sair")
#     print("5 - Limpar números")

#     opcao = input("Escolha uma opção: ")

#     if opcao == "1":
#         try:
#             numero = int(input("Digite um número: ").strip())
#             numeros.append(numero)
#             print(f"Número {numero} adicionado com sucesso!")
#         except ValueError:
#             print("Digite apenas números.")
#     elif opcao == "2":
#         print(f"Números digitados: {numeros}")
#     elif opcao == "3":
#         if numeros:
#             quantidade = len(numeros)
#             media = sum(numeros) / len(numeros)

#             print(f"Quantidade de números: {quantidade}")
#             print(f"Média: {media:.2f}")
#             print(f"Maior número: {max(numeros)}")
#             print(f"Menor número: {min(numeros)}")
#         else:
#             print("Nenhum número cadastrado.")
#     elif opcao == "4":
#         print("Saindo...")
#         break
#     elif opcao == "5":
#         numeros.clear()
#         print("Números limpos com sucesso!")
#     else:
#         print("Opção inválida. Por favor, escolha uma opção válida.")

# def adicionar_numero(lista):
#     try:
#         numero = int(input("Digite um número: ").strip())
#         lista.append(numero)
#         print(f"Número {numero} adicionado com sucesso!")
#     except ValueError:
#         print("Digite apenas números.")

# def mostrar_numeros(lista):
#     if lista:
#         print(f"Números digitados: {lista}")        
#     else:
#         print("Nenhum número digitado.")

# def mostrar_estatisticas(lista):
#     if lista:
#         quantidade = len(lista)
#         media = sum(lista) / len(lista)

#         print(f"Quantidade de números: {quantidade}")
#         print(f"Média: {media:.2f}")
#         print(f"Maior número: {max(lista)}")
#         print(f"Menor número: {min(lista)}")
#     else:
#         print("Nenhum número cadastrado.")          

# def limpar_numeros(lista):
#     lista.clear()
#     print("Números limpos com sucesso!")        

# numeros = []        
# while True:
#     print("\n--- MENU ---")
#     print("1 - Adicionar número")
#     print("2 - Ver números")
#     print("3 - Ver estatísticas")
#     print("4 - Sair")
#     print("5 - Limpar números")

#     opcao = input("Escolha uma opção: ")

#     if opcao == "1":
#         adicionar_numero(numeros)
#     elif opcao == "2":
#         mostrar_numeros(numeros)
#     elif opcao == "3":
#         mostrar_estatisticas(numeros)
#     elif opcao == "4":
#         print("Saindo...")
#         break
#     elif opcao == "5":
#         limpar_numeros(numeros)
#     else:
#         print("Opção inválida. Por favor, escolha uma opção válida.")
import json


def salvar_pessoas(lista):
    with open("pessoas.json", "w", encoding="utf-8") as arquivo:
        json.dump(lista, arquivo, indent=4, ensure_ascii=False)


def carregar_pessoas():
    try:
        with open("pessoas.json", "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)

    except FileNotFoundError:
        return []


def adicionar_pessoa(lista):
    nome = input("Digite o nome da pessoa: ").strip()

    try:
        idade = int(input("Digite a idade da pessoa: ").strip())

    except ValueError:
        print("Digite uma idade válida.")
        return

    pessoa = {
        "nome": nome,
        "idade": idade
    }

    lista.append(pessoa)

    salvar_pessoas(lista)

    print(f"{nome} adicionado(a) com sucesso!")


def mostrar_pessoas(lista):

    if lista:

        print("\n--- PESSOAS CADASTRADAS ---")

        for pessoa in lista:
            print(
                f"Nome: {pessoa['nome']} | "
                f"Idade: {pessoa['idade']}"
            )

    else:
        print("Nenhuma pessoa cadastrada.")


def buscar_pessoa(lista):

    nome_busca = input(
        "Digite o nome da pessoa que deseja buscar: "
    ).strip()

    for pessoa in lista:

        if pessoa["nome"].lower() == nome_busca.lower():

            print("\nPessoa encontrada!")
            print(f"Nome: {pessoa['nome']}")
            print(f"Idade: {pessoa['idade']}")

            return

    print("Pessoa não encontrada.")


def remover_pessoa(lista):

    nome_remover = input(
        "Digite o nome da pessoa que deseja remover: "
    ).strip()

    for pessoa in lista:

        if pessoa["nome"].lower() == nome_remover.lower():

            lista.remove(pessoa)

            salvar_pessoas(lista)

            print(f"{nome_remover} removido(a) com sucesso!")

            return

    print("Pessoa não encontrada.")


def limpar_pessoas(lista):

    lista.clear()

    salvar_pessoas(lista)

    print("Todas as pessoas foram removidas!")


# Carrega os dados do arquivo JSON
pessoas = carregar_pessoas()


while True:

    print("\n" + "=" * 30)
    print("      MENU PRINCIPAL")
    print("=" * 30)

    print("1 - Cadastrar pessoa")
    print("2 - Listar pessoas")
    print("3 - Buscar pessoa")
    print("4 - Remover pessoa")
    print("5 - Limpar pessoas")
    print("6 - Sair")

    opcao = input("\nEscolha uma opção: ").strip()

    if opcao == "1":
        adicionar_pessoa(pessoas)

    elif opcao == "2":
        mostrar_pessoas(pessoas)

    elif opcao == "3":
        buscar_pessoa(pessoas)

    elif opcao == "4":
        remover_pessoa(pessoas)

    elif opcao == "5":
        limpar_pessoas(pessoas)

    elif opcao == "6":
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida. Tente novamente.")