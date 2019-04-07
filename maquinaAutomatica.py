#Declarando as variaveis de preco e quantidade

#preco dos produtos
cocaValor = 3.50
pepsiValor = 3.50
guaranaValor = 3.50
mateleaoValor = 2.50
aguaValor = 2
energeticoValor = 8
acaiValor = 5.20

#quantidade de produtos
cocaEstoque = 6
pepsiEstoque = 9
guaranaEstoque = 7
mateleaoEstoque = 5
aguaEstoque = 10
energeticoEstoque = 7
acaiEstoque = 7

#quantidade de dinheiro
dezPapel = 3
cincoPapel = 6
doisPapel = 10
umReal = 14
cinquentaCentavos = 22
vinteCincoCentavos = 12
dezCentavos = 30
cincoCentavos = 17

#senha do administrador
senhaADM = 123456

#***********Codigo principal**************

while True:                                         #Repeticao para o usuario fazer varias operacoes
                                                    #Menu principal                             
    print ("\n" * 50) 
    print('************* MENU **************')
    print('*                               *')
    print('* 1: Comprar Bebida             *')
    print('* 2: Entrar como Administrador  *')
    print('*                               *')
    print('* 0: Encerrar                   *')
    print('*********************************')
    menu = input("Escolha a operacao: ")
                                                    #Escolha do menu
    if menu == "1":
        print("\n" * 50)
        print("  ---------------------------  ")
        print("| Codigo  -  Produto -  Valor |")
        print("|                             |")
        print("|  11          Coca  -  3.50  |")
        print("|  12          Água  -  2.00  |")
        print("|  13          Acaí  -  5.20  |")
        print("|  21         Pepsi  -  3.50  |")
        print("|  22       Guaraná  -  3.50  |")
        print("|  23     Mate Leão  -  2.50  |")
        print("|  31    Energético  -  8.00  |")
        print("  ---------------------------  ")
        opcao = input("Entre com o codigo do produto: ")
        
        if opcao == "11":
            print("Insira R$", cocaValor ,"na maquina.")
            if input("Entre com qualquer tecla se voce usara moedas no pagamento, se nao vai usar moedas apenas pressione Enter. "):
                umRealInserido = int(input("Quantas moedas de 1 real voce ira inserir ? "))
                cinquentaCEntavosInseridos = int(input("Quantas moedas de 50 centavos voce ira inserir ? "))
                vinteCincoCentavosInseridos = int(input("Quantas moedas de 25 centavos voce ira inserir ? "))
                dezCentavosInseridos = int(input("Quantas moedas de 10 centavos voce ira inserir ? "))
                cincoCentavosInseridos = int(input("Quantas moedas de 5 centavos voce ira inserir ? "))
                umReal += umRealInserido
                cinquentaCentavos += cinquentaCEntavosInseridos
                vinteCincoCentavos += vinteCincoCentavosInseridos
                dezCentavos += dezCentavosInseridos
                cincoCentavos += cincoCentavosInseridos
            else:
                print("")

    elif menu == "2":
        senhaEntrada = int(input("Entre com a senha do administrador: "))
        if senhaEntrada == senhaADM:
            while True:
                print("\n" * 50)
                print("        _______________________")
                print("        \ 1 = alterar estoque /")
                print("         \  2 = mudar senha  /")
                print("          \   3 = dinheiro  /")
                print("           \    4 = sair   /")
                print("            \ ----------- /")
                print("             \     A     /")
                print("              \    D    /")
                print("               \   M   /")
                print("                \  I  /")
                print("                 \ N /")
                print("                  \_/\n")
                opcao = input("Entre com o codigo da operacao desejada: ")
                if opcao == "1":
                    while True:
                        print("\n" * 50)
                        print("  ----------------------------")
                        print("| Codigo  -  Produto - Estoque")
                        print("|                             ")
                        print("|  11          Coca  - ", cocaEstoque ,"")
                        print("|  12          Água  - ", aguaEstoque ,"")
                        print("|  13          Acaí  - ", acaiEstoque ,"")
                        print("|  21         Pepsi  - ", pepsiEstoque ,"")
                        print("|  22       Guaraná  - ", guaranaEstoque ,"")
                        print("|  23     Mate Leão  - ", mateleaoEstoque ,"")
                        print("|  31    Energético  - ", energeticoEstoque ,"")
                        print("|                             ")
                        print("|  0 - para sair deste menu   ")
                        print("  ----------------------------")
                        if cocaEstoque > 20 or aguaEstoque > 20 or acaiEstoque > 20 or pepsiEstoque > 20 or guaranaEstoque > 20 or mateleaoEstoque > 20 or energeticoEstoque > 20:
                            print("\nUm ou mais dos valores do estoque parecem 1 pouco altos (maior que 20), talvez esteja incorreto ?\n")

                        opcaoEstoque = input("Entre com o codigo do produto: ")
                        if opcaoEstoque == "11":
                            cocaEstoque = int(input("\nVoce selecionou Coca-cola, entre com o novo valor de estoque do produto: "))
                        elif opcaoEstoque == "12":
                            aguaEstoque = int(input("\nVoce selecionou Agua, entre com o novo valor de estoque do produto: "))
                        elif opcaoEstoque == "13":
                            acaiEstoque = int(input("\nVoce selecionou Acai, entre com o novo valor de estoque do produto: "))
                        elif opcaoEstoque == "21":
                            pepsiEstoque = int(input("\nVoce selecionou Pepsi, entre com o novo valor de estoque do produto: "))
                        elif opcaoEstoque == "22":
                            guaranaEstoque = int(input("\nVoce selecionou Guarana, entre com o novo valor de estoque do produto: "))
                        elif opcaoEstoque == "23":
                            mateleaoEstoque = int(input("\nVoce selecionou Mate Leao, entre com o novo valor de estoque do produto: "))
                        elif opcaoEstoque == "31":
                            energeticoEstoque = int(input("\nVoce selecionou Energetico, entre com o novo valor de estoque do produto: "))
                        elif opcaoEstoque == "0":
                            break
                        else:
                            input("Codigo incorreto. Pressione Enter para continuar.")
                        



        else:
            input("Senha incorreta.")

    elif menu == "0":
        break

    else:
        input("Opcao incorreta. Pressione Enter para continuar.")
print("Obrigado por escolher a nossa maquina da Refrilandia!")
