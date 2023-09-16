print("Bem-vindo a Loja do Alan Coelho!") # Essa linha imprime uma mensagem de boas vindas para o usuario.

valor_unitario = float(input("Digite o valor do produto: ")) #Pede para que o usuario digite o valor unitario do produto e a quantidade.
quantidade = int(input("Digite a quantidade do produto: "))

desconto = 0

if quantidade < 200:            #Quantidade for menor que 200, não há desconto.
    desconto = 0
else:
    if quantidade < 1000:       #Quantidade estiver entre 200 e 999, o desconto é de 5%.
        desconto = 5
    elif quantidade < 2000:   #Quantidade estiver entre 1000 e 1999, o desconto é de 10%.
            desconto = 10
    else:
        desconto = 15       #Quantidade for 2000 ou mais, o desconto é de 15%.

valor_total_sem_desconto = valor_unitario * quantidade                  #Calculo da valor e quantidade.
valor_desconto = valor_total_sem_desconto * (desconto / 100)            #Aqui seria o valor do anterior (sem desconto) multiplicado por (variavel desconto/100).
valor_total_com_desconto = valor_total_sem_desconto - valor_desconto    #Valor total com o desconto aplicado.

print("\nPedido recebido. Seu desconto é de {}% por unidade.".format(desconto)) #Apresenta ao usuario as informacoes da compra: o descoto, valor sem desconto e com desconto.
print("Valor total SEM desconto: R$ {:.2f}".format(valor_total_sem_desconto))
print("Valor total COM desconto: R$ {:.2f}".format(valor_total_com_desconto))
print("OBRIGADO PELA COMPRA, VOLTE SEMPRE!")
