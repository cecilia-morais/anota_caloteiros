import os
import pickle
import datetime

caloteiros ={}
deves = {}



try:   #recuperar os arquivos 
    arqcalote = open("caloteiros.dat", "rb")
    calotes = pickle.load(arqcalote)
    caloteiros = calotes[1]
    deves = calotes[2]
    arqcalote.close()
except:
    arqcalote = open("caloteiros.dat", "wb")
    arqcalote.close()

def salvar_caloteiros():
    calotes = {
        1: caloteiros,
        2: deves
    }
    arqcalote = open("caloteiros.dat", "wb")
    pickle.dump(calotes, arqcalote)
    arqcalote.close()

   
def calcular_total_com_juros(quantia, juros):
        total = quantia + (quantia * juros / 100)
        return total


def verificar_data_pagamento(caloteiros, deves):
    data_atual = datetime.date.today()
    mensagem_aviso = ""

    for caloteiro, dados_caloteiro in caloteiros.items():
        data_devolve = datetime.datetime.strptime(dados_caloteiro['data_devolve'], "%d/%m/%Y").date()
        if data_devolve <= data_atual:
            print()
            mensagem_aviso += f"AVISO: A data de pagamento do caloteiro {caloteiro} está atrasada!\n"

    for devedor, dados_devedor in deves.items():
        data_pagamento = datetime.datetime.strptime(dados_devedor['data_pagamento'], "%d/%m/%Y").date()
        if data_pagamento <= data_atual:
            print()
            mensagem_aviso += f"AVISO: A data de pagamento da sua conta {devedor} está atrasada!\n"

    return mensagem_aviso




def menu():
    os.system("cls || clear")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("$$$$$                           ANOTA CALOTEIROS                         $$$$$")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("$$$$$                    O QUE VOSSA SENHORIA DESEJAS?                   $$$$$")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("$$$$$ 1 - ENTRAR NA ÁREA CALOTEIRO                                       $$$$$")
    print("$$$$$ 2 - ENTRAR NA ÁREA DE QUEM TU DEVES                                $$$$$")
    print("$$$$$ 3 - SAIR                                                           $$$$$")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print()
    area = input("$$$$$ DIGITE A ÁREA DESEJADA: ")
    print()
    return area

def menu_caloteiro():
    os.system("cls || clear")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("$$$$$                           ANOTA CALOTEIROS                         $$$$$")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("$$$$$                    O QUE VOSSA SENHORIA DESEJAS?                   $$$$$")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("$$$$$ 1 - CADASTRAR CALOTEIRO                                            $$$$$")
    print("$$$$$ 2 - LISTAR CALOTEIROS                                              $$$$$")
    print("$$$$$ 3 - ALTERAR CALOTEIRO                                              $$$$$")
    print("$$$$$ 4 - MARCAR QUE O CALOTEIIRO TE PAGOU                               $$$$$")
    print("$$$$$ 5 - SAIR                                                           $$$$$")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print()
    caloteiro = input("$$$$$ DIGITE A ÁREA DESEJADA: ")
    print()
    return caloteiro

def cadastrar_caloteiro():
    os.system("cls || clear")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("$$$$$                           ANOTA CALOTEIROS                         $$$$$")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("$$$$$                     CADASTRE SEU CALOTEIRO AQUI                    $$$$$")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print()
    nome = input("$$$$$ DIGITE O NOME DO CALOTEIRO: ")
    print()
    idade = int(input("$$$$$ DIGITE A IDADE DO CALOTEIRO: "))
    print()
    endereco = input("$$$$$ DIGITE O ENDEREÇO DO CALOTEIRO: ")
    print()
    telefone = input("$$$$$ DIGITE O TELEFONE DO CALOTEIRO: ")
    print()
    email = input("$$$$$ DIGITE O EMAIL DO CALOTEIRO: ")
    print()
    quantia = float(input("$$$$$ DIGITE A QUANTIA QUE O CALOTEIRO TE DEVE: "))
    print()
    juros = float(input("$$$$$ DIGITE PORCENTAGEM DE JUROS ADICIONADO A QUANTIA INICIAL: "))
    print()
    total_com_juros = calcular_total_com_juros(quantia, juros)
    print("$$$$$ O total com juros fica: R$%.2f "  %total_com_juros)
    print()
    data_pegou = input("$$$$$ DIGITE A DATA QUE O CALOTEIRO TE PEDIU GRANA EMPRESTADO (dd/mm/aaaa): ")
    print()
    data_devolve = input("$$$$$ DIGITE A DATA QUE O CALOTEIRO DISSE QUE IRIA DEVOLVER A GRANA (dd/mm/aaaa): ")
    print()
    if not bool(caloteiros):
        caloteiros[1]=[1, nome, idade, endereco, telefone, email, quantia, juros, total_com_juros, data_pegou, data_devolve]
        salvar_caloteiros()
        
    else:
        ultima_chave = list(caloteiros.keys())[-1]
        id = ultima_chave + 1
        caloteiros[id]=[id, nome, idade, endereco, telefone, email, quantia, juros, total_com_juros, data_pegou, data_devolve]
        salvar_caloteiros()

    print("$$$$$ CADASTRO REALIZADO COM SUCESSO! $$$$$")
    print()
    input("Tecle ENTER para continuar...")
    print()

def listar_caloteiros():
    os.system("cls || clear")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("$$$$$                           ANOTA CALOTEIROS                         $$$$$")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("$$$$$                         LISTA DE CALOTEIROS                        $$$$$")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print()
    if not bool(caloteiros):
        print("$$$$$ NÃO HÁ CALOTEIROS CADASTRADOS! $$$$$")
        print()
    else:
        for i in caloteiros:
            print("$$$$$ CALOTEIRO  ", caloteiros[i][0])
            print("$$$$$ NOME: ", caloteiros[i][1])
            print("$$$$$ IDADE: ", caloteiros[i][2])
            print("$$$$$ ENDEREÇO: ", caloteiros[i][3])
            print("$$$$$ TELEFONE: ", caloteiros[i][4])
            print("$$$$$ EMAIL: ", caloteiros[i][5])
            print("$$$$$ QUANTIA: ", caloteiros[i][6])
            print("$$$$$ JUROS: ", caloteiros[i][7])
            print("$$$$$ TOTAL COM JUROS: ", caloteiros[i][8])
            print("$$$$$ DATA QUE PEGOU: ", caloteiros[i][9])
            print("$$$$$ DATA QUE DEVOLVE: ", caloteiros[i][10])
            if caloteiros[i][10] == "PAGO":
                print("O CALOTEIRO JÁ TE PAGOU!")
            print("______________________________________________________________________________")
            print()
    input("Tecle ENTER para continuar...")
    print()

def alterar_caloteiro():
    os.system("cls || clear")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("$$$$$                           ANOTA CALOTEIROS                         $$$$$")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("$$$$$                          ALTERAR CALOTEIRO                         $$$$$")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")  
    print()
    id = int(input("$$$$$ DIGITE O ID DO CALOTEIRO QUE DESEJA ALTERAR: "))
    print()
    if id in caloteiros:
        print("Digite o que deseja alterar: ")
        print("1 - NOME")
        print("2 - IDADE")
        print("3 - ENDEREÇO")
        print("4 - TELEFONE")
        print("5 - EMAIL")
        print("6 - QUANTIA")
        print("7 - JUROS")
        print("8 - DATA QUE PEGOU")
        print("9 - DATA QUE DEVOLVE")
        print()
        opcao = int(input("$$$$$ DIGITE A OPÇÃO DESEJADA: "))
        print()
        if opcao == 1:
            nome = input("$$$$$ DIGITE O NOVO NOME: ")
            print()
            caloteiros[id][1] = nome
            salvar_caloteiros()
        elif opcao == 2:
            idade = int(input("$$$$$ DIGITE A NOVA IDADE: "))
            print()
            caloteiros[id][2] = idade
            salvar_caloteiros()
        elif opcao == 3:
            endereco = input("$$$$$ DIGITE O NOVO ENDEREÇO: ")
            print()
            caloteiros[id][3] = endereco
            salvar_caloteiros()
        elif opcao == 4:
            telefone = input("$$$$$ DIGITE O NOVO TELEFONE: ")
            print()
            caloteiros[id][4] = telefone
            salvar_caloteiros()
        elif opcao == 5:
            email = input("$$$$$ DIGITE O NOVO EMAIL: ")
            print()
            caloteiros[id][5] = email
            salvar_caloteiros()
        elif opcao == 6:
            quantia = float(input("$$$$$ DIGITE A NOVA QUANTIA: "))
            print()
            caloteiros[id][6] = quantia
            juros = caloteiros[id][7]
            total = quantia + (quantia * juros / 100)
            print("$$$$$ O total com juros fica: R$%.2f "  %total)
            print()
            salvar_caloteiros()
        elif opcao == 7:
            juros = float(input("$$$$$ DIGITE O NOVO JUROS: "))
            print()
            caloteiros[id][7] = juros
            quantia = caloteiros[id][6]
            total = quantia + (quantia * juros / 100)
            print("$$$$$ O total com juros fica: R$%.2f "  %total)
            print()
            salvar_caloteiros()
        elif opcao == 8:
            data_pegou = input("$$$$$ DIGITE A NOVA DATA QUE PEGOU (dd/mm/aaaa): ")
            print()
            caloteiros[id][8] = data_pegou
            salvar_caloteiros()
        elif opcao == 9:
            data_devolve = input("$$$$$ DIGITE A NOVA DATA QUE DEVOLVE (dd/mm/aaaa): ")
            print()
            caloteiros[id][9] = data_devolve
            salvar_caloteiros()
        else:
            print("$$$$$ OPÇÃO INVÁLIDA! $$$$$")
            print()


        print("$$$$$ ALTERAÇÃO REALIZADA COM SUCESSO! $$$$$")
    else:
        print("$$$$$ CALOTEIRO NÃO ENCONTRADO! $$$$$")
        print()

def marcar_pago():
    os.system("cls || clear")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("$$$$$                           ANOTA CALOTEIROS                         $$$$$")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("$$$$$                          MARCAR PAGO                               $$$$$")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print()
    id = int(input("$$$$$ DIGITE O ID DO CALOTEIRO QUE DESEJA MARCAR COMO PAGO: "))
    print()
    if id in caloteiros:
        caloteiros[id][10] = "PAGO"
        salvar_caloteiros()
        print("$$$$$ MARCAÇÃO REALIZADA COM SUCESSO! $$$$$")
        print()
    else:
        print("$$$$$ CALOTEIRO NÃO ENCONTRADO! $$$$$")
        print()
    
    input("Tecle ENTER para continuar...")
    print()


def menu_devedor():
    os.system("cls || clear")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("$$$$$                           ANOTA CALOTEIROS                         $$$$$")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("$$$$$                    O QUE VOSSA SENHORIA DESEJAS?                   $$$$$")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("$$$$$ 1 - CADASTRAR A QUEM TU DEVES                                      $$$$$")
    print("$$$$$ 2 - LISTAR QUEM TU DEVES                                           $$$$$")
    print("$$$$$ 3 - ALTERAR QUEM TU DEVES                                          $$$$$")
    print("$$$$$ 4 - MARCAR QUE TU PAGOU ALGUÉM                                     $$$$$")
    print("$$$$$ 5 - SAIR                                                           $$$$$")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print()
    devedor = input("$$$$$ DIGITE A ÁREA DESEJADA: ")
    print()
    return devedor

def cadastrar_devedor():
    os.system("cls || clear")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("$$$$$                           ANOTA CALOTEIROS                         $$$$$")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$") 
    print("$$$$$                     CADASTRE QUEM TU DEVES AQUI                   $$$$$")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print()
    nome = input("$$$$$ DIGITE O NOME DE QUEM TU DEVES: ")
    print()
    quantia = float(input("$$$$$ DIGITE A QUANTIA QUE TU DEVES: "))
    print()
    res = input("$$$$$ TEM JUROS: \n 1 - SIM \n 2 - NÃO \n")
    print()
    if res == "1":
        juros = float(input("$$$$$ DIGITE A PORCENTAGEM DE JUROS: "))
        print()
        total_com_juros = calcular_total_com_juros(quantia, juros)
        print("$$$$$ O total com juros fica: R$%.2f "  %total_com_juros)
        print()
    else:
        print("$$$$$ OK, SEM JUROS, MAS NÃO VAI ESQUECER DE PAGAR HEIN! ")
        print()
        juros = 0

    data_pegou = input("$$$$$ DIGITE A DATA QUE TU PEGOU EMPRESTADO (dd/mm/aaaa): ")
    print()

    data_devolve = input("$$$$$ DIGITE A DATA QUE TU VAI DEVOLVER (dd/mm/aaaa): ")
    print()

    if not bool(deves):
        deves[1]=[1, nome, quantia, juros, total_com_juros, data_pegou, data_devolve]
        salvar_caloteiros()
        
    else:
        ultima_chave = list(deves.keys())[-1]
        id = ultima_chave + 1
        deves[id]=[id, nome, quantia, juros, total_com_juros, data_pegou, data_devolve]
        salvar_caloteiros()
    
    print("$$$$$ CADASTRO REALIZADO COM SUCESSO! $$$$$")
    print()

def listar_devedores():
    os.system("cls || clear")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("$$$$$                           ANOTA CALOTEIROS                         $$$$$")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("$$$$$                        LISTA DE QUEM TU DEVES                      $$$$$")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print()
    if not bool(deves):
        print("$$$$$ NÃO HÁ DEVEDORES CADASTRADOS! $$$$$")
        print()
    else:
        print("$$$$$ ESSAS SÃO SUAS CONTAS:")
        print()
        for i in deves:
            print("$$$$$ CONTA Nº ", deves[i][0])
            print("$$$$$ NOME: ", deves[i][1])
            print("$$$$$ QUANTIA: ", deves[i][2])
            print("$$$$$ JUROS: ", deves[i][3])
            print("$$$$$ TOTAL COM JUROS: ", deves[i][4])
            print("$$$$$ DATA QUE PEGOU: ", deves[i][5])
            print("$$$$$ DATA QUE DEVOLVE: ", deves[i][6])
            if deves[i][6] == "PAGO":
                print("$$$$$ VOCÊ JA PAGOU ESSA CONTA!")
                print("$$$$$ DATA QUE PAGOU: ", deves[i][7])
            print("______________________________________________________________________________")
            print()
    input("Tecle ENTER para continuar...")
    print()



def alterar_devedor():
    os.system("cls || clear")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("$$$$$                           ANOTA CALOTEIROS                         $$$$$")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("$$$$$                           ALTERAR DEVEDOR                          $$$$$")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print()
    id = int(input("$$$$$ DIGITE O ID DO DEVEDOR QUE DESEJA ALTERAR: "))
    print()
    if id in deves:
        print("Digite o que deseja alterar: ")
        print("1 - NOME")
        print("2 - QUANTIA")
        print("3 - JUROS")
        print("4 - DATA QUE PEGOU")
        print("5 - DATA QUE DEVOLVE")
        print()
        opcao = int(input("$$$$$ DIGITE A OPÇÃO DESEJADA: "))
        print()
        if opcao == 1:
            nome = input("$$$$$ DIGITE O NOVO NOME: ")
            print()
            deves[id][1] = nome
            salvar_caloteiros()
        elif opcao == 2:
            quantia = float(input("$$$$$ DIGITE A NOVA QUANTIA: "))
            print()
            deves[id][2] = quantia
            juros = deves[id][3]
            total = quantia + (quantia * juros / 100)
            print("$$$$$ O total com juros fica: R$%.2f "  %total)
            print()
            salvar_caloteiros()
        elif opcao == 3:
            juros = float(input("$$$$$ DIGITE O NOVO JUROS: "))
            print()
            deves[id][3] = juros
            quantia = deves[id][2]
            total = quantia + (quantia * juros / 100)
            print("$$$$$ O total com juros fica: R$%.2f "  %total)
            print()
            salvar_caloteiros()
        elif opcao == 4:
            data_pegou = input("$$$$$ DIGITE A NOVA DATA QUE PEGOU (dd/mm/aaaa): ")
            print()
            deves[id][5] = data_pegou
            salvar_caloteiros()
        elif opcao == 5:
            data_devolve = input("$$$$$ DIGITE A NOVA DATA QUE VAI DEVOLVER, CABA SAFADO (dd/mm/aaaa): ")
            print()
            deves[id][6] = data_devolve
            salvar_caloteiros()
        else:
            print("$$$$$ OPÇÃO INVÁLIDA! $$$$$")
            print()


        print("$$$$$ ALTERAÇÃO REALIZADA COM SUCESSO! $$$$$")
    else:
        print("$$$$$ DEVEDOR NÃO ENCONTRADO! $$$$$")
        print()
    
    input("Tecle ENTER para continuar...")
    print()

def excluir_devedor():
    os.system("cls || clear")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("$$$$$                           ANOTA CALOTEIROS                         $$$$$")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("$$$$$                         MARCAR QUE TU PAGOU                        $$$$$")
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print()
    id = int(input("$$$$$ DIGITE O ID DO DEVEDOR QUE DESEJA MARCAR QUE PAGOU: "))
    print()
    if id in deves:
        da = datetime.datetime.now().strftime("%d/%m/%Y")
        deves[id][6] = "PAGO"
        deves[id][7] = da
        salvar_caloteiros()
        print("$$$$$ DEVEDOR PAGO COM SUCESSO, PARABÉNS! $$$$$")
        print()
    else:
        print("$$$$$ DEVEDOR NÃO ENCONTRADO! $$$$$")
        print()
    
    input("Tecle ENTER para continuar...")
    print()

def tela_inicial():
    os.system("cls || clear")
    print("$"*80)
    print("$$$$$                         ANOTA CALOTEIROS                         $$$$$")
    print("$"*80)
    print("$$$$$                  BEM VINDO AO ANOTA CALOTEIROS!                  $$$$$")
    print("$"*80)
    print()

    input("Tecle ENTER para continuar...")
    print()

tela_inicial()
verificar_data_pagamento(caloteiros, deves)
area = menu()
while area != "3":
    if area == "1":
        caloteiro = menu_caloteiro()
        while caloteiro != "5":
            if caloteiro == "1":
                cadastrar_caloteiro()
            elif caloteiro == "2":
                listar_caloteiros()
            elif caloteiro == "3":
                alterar_caloteiro()
            elif caloteiro == "4":
                marcar_pago()
            else:
                print("$$$$$ OPÇÃO INVÁLIDA! $$$$$")
                print()
            caloteiro = menu_caloteiro()
    elif area == "2":
        devedor = menu_devedor()
        while devedor != "5":
            if devedor == "1":
                cadastrar_devedor()
            elif devedor == "2":
                listar_devedores()
            elif devedor == "3":
                alterar_devedor()
            elif devedor == "4":
                excluir_devedor()
            else:
                print("$$$$$ OPÇÃO INVÁLIDA! $$$$$")
                print()
            devedor = menu_devedor()
    else:
        print("$$$$$ OPÇÃO INVÁLIDA! $$$$$")
        print()
    area = menu()

print("$$$$$ OBRIGADO POR USAR O ANOTA CALOTEIROS! $$$$$")
print()
print("$$$$$ VOLTE SEMPRE! $$$$$")