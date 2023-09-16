print("Bem vindo ao Controle de Colaboradores do Alan Coelho Gomes")            #A. Realizar o print uma mensagem de boas-vindas que apareça o seu nome;
lista_colaboradores = []                                                        #B. Deve-se criar uma lista vazia com o nome de lista_colaboradores e a variável id_global com valor inicial igual a 0;
id_global = 0                                                                   #G.Deve-se utilizar lista de dicionários (Cada colaborador e um dicionario ou seja a lista de colaboradores e uma lista de dicionarios.);

def borda(phrase):                                                              #criei uma funcao para os menus.
    tam = len(phrase)
    if tam:
        print('=' * 50)
        print(f'{phrase.center(50).upper()}')
        print('=' * 50)

def end_borda():
    print('*' * 50)

def cadastrar_colaborador(id):                                                  #C. Deve-se criar uma função chamada cadastrar_colaborador(id);
    global id_global
    borda('menu cadastrar')           
    nome = input("Entre com o nome do colaborador: ")                           #C.a Pergunta nome, setor, pagamento do colaborador; 
    setor = input("Entre com o setor do colaborador: ")
    pagamento = float(input("Entre com o pagamento do colaborador: "))
    dicionario_colaborador = {"id": id,                                         #C.b Armazena o id (este é fornecido via parâmetro da função), nome, setor, salário dentro de um dicionário;
                              "nome": nome,
                              "setor": setor,
                              "pagamento": pagamento}
    lista_colaboradores.append(dicionario_colaborador)                          #C.c Copiar o dicionário dentro para dentro da da lista_colaboradores; 
    end_borda()

def consultar_colaborador():                                                    #D. Deve-se criar uma função chamada consultar_colaborador();
    while True:
        borda('menu colaborador')
        opcao_consultar = input("\nEscolha a opção desejada:\n"+                #D.a Deve-se pergunta qual opção deseja (1. Consultar Todos / 2. Consultar por Id / 3. Consultar por Setor / 4. Retornar ao menu);
                                "1-Consultar TODOS os Colaboradores\n"+
                                "2-Consultar Colaborador por ID\n"+
                                "3-Consultar Colaboradores por SETOR\n"+
                                "4-Retornar ao menu\n"+
                                ">>")
        end_borda()

        if opcao_consultar == "1":                                              #D.a.i Se Consultar Todos, apresentar todos os colaboradores com todos os seus dados cadastrado;
            print("Você escolheu a opção consultar TODOS os colaboradores")
            print("------------------------")
            for colaborador in lista_colaboradores:
                for key, value in colaborador.items():
                    print('{}: {}'.format(key, value))
            print("------------------------")        
        elif opcao_consultar == "2":                                            #D.a.ii Se Consultar por Id, apresentar o colaborador específico com todos os seus dados cadastrados; 
            print("Consultar Colaborador por ID")
            id_desejado = int(input("Entre com o ID do colaborador: "))
            for colaborador in lista_colaboradores:
                if colaborador["id"] == id_desejado:
                    print("------------------------")
                    for key, value in colaborador.items():
                        print("{}: {}".format(key, value))
                    print("------------------------")
                    break
            else:
                print("Colaborador com ID {} não encontrado.".format(id_desejado))
        elif opcao_consultar == "3":                                            #D.a.iii Se Consultar por Setor, apresentar todos os colaboradores do setor específico com todos os seus dados cadastrados; 
            print("Consultar Colaboradores por SETOR")
            setor_desejado = input("Entre com o SETOR: ")
            for colaborador in lista_colaboradores:
                if colaborador["setor"].lower() == setor_desejado.lower():
                    print("------------------------")
                    for key, value in colaborador.items():
                        print("{}: {}".format(key, value))
                    print("------------------------")
        elif opcao_consultar == "4":                                            #D.a.iv Se Retornar ao menu, deve-se retornar ao menu principal;
            return
        else:
            print("Opção Inválida. Tente novamente")                            #D.a Realizar o print “Opção inválida" se entrar com valor diferente de 1, 2, 3 ou 4;
            continue
        
def remover_colaborador():                                                      #E. Deve-se criar uma função chamada remover_colaborador();
    borda('menu remover colaborador')
    id_desejado = int(input("Entre com o ID do colaborador a ser removido: "))  #E.a Deve-se pergunta pelo id do colaborador a ser removido; 
    for colaborador in lista_colaboradores:
        if colaborador["id"] == id_desejado:
            lista_colaboradores.remove(colaborador)                             #E.b Remover o colaborador da lista_colaboradores;
            break
    else:
        print("Colaborador com ID {} não encontrado.".format(id_desejado))  
    end_borda()

def main():                                                                     #F. Deve-se criar uma estrutura de menu no main 
    global id_global
    while True:
        borda('menu principal')
        opcao_menu = input("\nEscolha a opção desejada:\n"+                     #F.a Deve-se pergunta qual opção deseja (1. Cadastrar Colaborador / 2. Consultar Colaborador / 3. Remover Colaborador / 4. Encerrar Programa);
                           "1-Cadastrar Colaborador\n"+                         
                           "2-Consultar Colaborador\n"+
                           "3-Remover Colaborador\n"+
                           "4-Encerrar Programa\n"+
                           ">>")
        end_borda()
        
        if opcao_menu == "1":
            id_global += 1                                                      #F.a.i Se Cadastrar Colaborador, acrescentar em um a variavel id_ global e chamar a função cadastrar_colaborador(id_ global); 
            cadastrar_colaborador(id_global)            
        elif opcao_menu == "2":                                                 #F.a.ii Se Consultar Colaborador, chamar função consultar_colaborador(); 
            consultar_colaborador()
        elif opcao_menu == "3":                                                 #F.a.iii Se Remover Colaborador, chamar função remover_colaborador(); 
            remover_colaborador()
        elif opcao_menu == "4":
            print("Encerrando o programa...")       
            break                                                               #F.a.iv Se Encerrar Programa, sair do menu (e com isso acabar a execução do código); #Encerra o laco menu e o programa acaba.
        else:
            print("Opção Inválida. Tente novamente.")                           #F.a Realizar o print “Opção inválida" se entrar com valor diferente de 1, 2, 3 ou 4 ;
            continue

if __name__ == "__main__":
    main()