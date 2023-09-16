def boas_vindas():
    print("-"*50)
    print("      Bem-vindo ao petshop do Alan Coelho!")
    print("-"*50)
def cachorro_peso():
    while True:
        try:
            peso = float(input("Digite o peso do cachorro em kg: "))
            print("-"*50)
            if peso < 3:
                return 40
            elif peso < 10:
                return 50
            elif peso < 30:
                return 60
            elif peso < 50:
                return 70
            else:
                print("O petshop não aceita cães com peso igual ou maior que 50 kg.")
        except ValueError:
            print("Por favor, digite um valor numérico válido.")
        
def cachorro_pelo():
    while True:
        tipo_pelo = input ("Pelo do cachorro: \n"+
                           "c - Pelo Curto\n"+
                           "m - Pelo Medio\n"+
                           "L - Pelo Longo\n"+
                           ">>").lower()
        print("-"*50)
        if tipo_pelo == 'c':
            return 1
        elif tipo_pelo == 'm':
            return 1.5
        elif tipo_pelo == 'l':
            return 2
        else:
            print("Opção inválida. O tipo de pelo deve ser 'c', 'm' ou 'l'.")

def cachorro_extra():
    valor_extra = 0
    while True: 
        adicional = input("Servicos adicionais disponiveis: \n"+
                          "1 - Cortar unhas (R$ 10,00)\n"+
                          "2 - Escovar os dentes (R$12,00)\n"+
                          "3 - Limpar orelhas (R$15,00)\n"+
                          "0 - Nao quero servicos adicionais.\n"+
                          ">>")
        print("-"*50)
        if adicional == '0':
            return valor_extra
        elif adicional in ('1', '2', '3'):
            if adicional == '1':
                valor_extra += 10
            elif adicional == '2':
                valor_extra += 12
            elif adicional == '3':
                valor_extra += 15
            else:
                print("Opção inválida. Escolha entre 0, 1, 2 ou 3.")

def main():
    boas_vindas()
    try:
        peso_base = cachorro_peso()
        multiplicador_pelo = cachorro_pelo()
        valor_extra = cachorro_extra()

        # Calculando o valor total a pagar
        valor_total = peso_base * multiplicador_pelo + valor_extra

        print(f"Total a pagar é: R$ {valor_total:.2f}(peso: {peso_base} * {multiplicador_pelo} + adicional(is): {valor_extra})")
        print("OBRIGADO, VOLTE SEMPRE!")
    except ValueError as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()