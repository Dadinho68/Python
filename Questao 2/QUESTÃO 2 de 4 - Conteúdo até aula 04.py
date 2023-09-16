print("Bem-vindo(a) ao aplicativo de vendas da Sorveteria do Alan Coelho!")  # Boas Vindas
print("--------------------------------------------- MENU ---------------------------------------------")
print("|   N⁰ DE BOLAS     |   SABOR TRADICIONAL (tr)  |   SABOR PREMIUM (pr)  |  SABOR ESPECIAL (es) |")
print("|        1          |        R$ 6,00            |       R$ 7,00         |       R$ 8,00        |")  # Menu de sabores(Esses sao os valores do enuciado, diferentes do menu do exemplo de saida.)
print("|        2          |        R$ 11,00           |       R$ 13,00        |       R$ 15,00       |")
print("|        3          |        R$ 15,00           |       R$ 18,00        |       R$ 21,00       |")
print("------------------------------------------------------------------------------------------------")

def calcular_valor(sabor, quantidade):  # Recebe o sabor e a quantidade de bolas do sorvete e verifica para calcular o valor total do pedido.
    if sabor == "tr":
        if quantidade == 1:
            return 6
        elif quantidade == 2:
            return 11
        elif quantidade == 3:
            return 15
    elif sabor == "pr":
        if quantidade == 1:
            return 7
        elif quantidade == 2:
            return 13
        elif quantidade == 3:
            return 18
    elif sabor == "es":
        if quantidade == 1:
            return 8
        elif quantidade == 2:
            return 15
        elif quantidade == 3:
            return 21
    return None

valor_total_pedido = 0  # Inicializa o valor total do pedido como zero

while True:  # Loop para interação com o cliente.
    sabor = input("\nDigite o sabor do sorvete (tr - Tradicional, pr - Premium, es - Especial): ")

    if sabor not in ["tr", "pr", "es"]:
        print("\nSabor de Sorvete Inválido. Tente novamente.")  # Mensagem de erro aparecerá caso não seja um sabor válido.
        continue

    quantidade = int(input("Digite o número de bolas de sorvete desejado (1/2/3): "))

    if quantidade not in [1, 2, 3]:
        print("\nQuantidade de Bolas de Sorvete Inválida. Tente novamente.")  # O mesmo para a quantidade de bolas.
        continue

    valor_total_pedido += calcular_valor(sabor, quantidade)  # Atualiza o valor total do pedido com o valor do novo pedido
    print(f"Valor do pedido: R${calcular_valor(sabor, quantidade):.2f}")

    pedido_adicional = input("Deseja pedir mais alguma coisa? (s/n): ")

    if pedido_adicional.lower() != 's':
        break

print("\nObrigado! ")
print(f"Valor total do pedido: R${valor_total_pedido:.2f}")  # Exibe o valor total de todos os pedidos feitos pelo cliente
