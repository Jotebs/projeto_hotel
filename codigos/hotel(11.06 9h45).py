#FUNÇÕES PARA OS ARQUIVOS
def existe_arquivo(nome):
    import os
    if os.path.exists(nome):
        return True
    else:
        return False
    

def carregar_dados_arquivos_cliente(lista_cliente):
    if existe_arquivo("Clientes.txt"):
        arq = open("Clientes.txt", 'r', encoding="utf-8")
        for linha in arq:
            #CLIENTE - nome, cpf, endereço, telefones fixo e celular
            cliente = []
            linha = linha.strip().split(';')
            
            #insere o nome
            cliente.append(linha[0])
            #insere cpf
            cliente.append(linha[1])
            #insere o endereço
            cliente.append(linha[2])
            #insere a data de nascimento
            cliente.append(linha[3])
            #insere o telefone fixo
            cliente.append(linha[4])
            #insere o telefone celular
            cliente.append(linha[5])
            
            lista_cliente.append(cliente)
        arq.close()
            

def gravar_dados_cliente(lista_cliente):
    arq = open("Clientes.txt", 'w', encoding="utf-8")
    for i in range(len(lista_cliente)):
        contato = ''
        # nome;cpf;endereço;data_nascimento;telefones_\n
        contato += lista_cliente[i][0] + ';' +  lista_cliente[i][1] + ';' + lista_cliente[i][2] + ';' +  lista_cliente[i][3] + ';' +  f"{lista_cliente[i][4]}" + ';' + f"{lista_cliente[i][5]}" + '\n'                 
        arq.write(contato)
    arq.close()

#--------------------------------------------------------
#DAQUI PRA BAIXO É A ÁREA DE CLIENTES
#--------------------------------------------------------

def incluir_cliente(lista_clientes):
    cliente = []

    nome = input("Digite o nome do cliente: ")
    cliente.append(nome)
    
    #CPF tem as limitações pois é atributo CHAVE
    cpf = input("Digite o CPF do cliente: ").replace(" ", "")
    if len(cpf) < 11 or len(cpf) > 14:
        print("Digite corretamente o CPF.")
        return
    else:
        cpf = cpf.replace(".", "").replace("-", "")
        for i in range(len(lista_clientes)):
            if cpf == lista_clientes[i][1]:
                print()
                print("Esse CPF já está cadastrado.")
                return
            
        if cpf.isdigit() and cpf not in lista_clientes:
            cliente.append(cpf)
        else:
            print("Verifique se o cpf está digitado corretamente e tente novamente.")
            return 
            

    endereco = input("Digite o endereço do cliente: ")
    cliente.append(endereco)

    nascimento = input("Digite a data de nascimento do cliente(xx/xx/xxxx): ")
    cliente.append(nascimento)

    tel_fixo = int(input("Digite o telefone fixo do ciente: "))
    celular = int(input("Digite o telefone celular do ciente: "))
    cliente.append(tel_fixo)
    cliente.append(celular)

    lista_clientes.append(cliente)
    print()
    print("Cliente adicionado com sucesso.")
    


def imprimir_um_cliente(lista_clientes, indice):
    print("------------------------------------------")
    print(f"Cliente: {lista_clientes[indice][0]}")
    print(f"CPF: {lista_clientes[indice][1]}")
    print(f"Endereço: {lista_clientes[indice][2]}")
    print(f"Data de nascimento: {lista_clientes[indice][3]}")
    print(f"Telefone fixo: {lista_clientes[indice][4]}")
    print(f"Telefone celular: {lista_clientes[indice][5]}")
    print("------------------------------------------")



def listar_um_cliente(lista_clientes):
    if len(lista_clientes) == 0:
        print()
        print("A lista de clientes está vazia.")
        print()
    else:
        busca = input("Digite o cpf do cliente para a busca: ").replace(".", "").replace("-", "")
        achou = False
        for i in range(len(lista_clientes)):
            if busca == lista_clientes[i][1]:
                achou = True
        if not achou:
            print("Não existe um cliente com esse CPF.")
        else:
            for i in range(len(lista_clientes)):
                if busca == lista_clientes[i][1]:
                    imprimir_um_cliente(lista_clientes, i)



def listar_todos_clientes(lista_clientes):
    
    if len(lista_clientes) == 0:
        print()
        print("A lista de clientes está vazia.")
        print()
    else:
        print("---------------LISTA DE CLIENTES---------------")
        for i in range(len(lista_clientes)):
            print(f"Cliente: {lista_clientes[i][0]}")
            print(f"CPF: {lista_clientes[i][1]}")
            print(f"Endereço: {lista_clientes[i][2]}")
            print(f"Data de nascimento: {lista_clientes[i][3]}")
            print(f"Telefone fixo: {lista_clientes[i][4]}")
            print(f"Telefone celular: {lista_clientes[i][5]}")
            print("------------------------------------------")



def alterar_cliente(lista_clientes):
    if len(lista_clientes) == 0:
        print()
        print("A lista de clientes está vazia.")
        print()
    else:
        busca = input("Digite o cpf do cliente para a busca: ").replace(".", "").replace("-", "")
        achou = False
        for i in range(len(lista_clientes)):
            if busca == lista_clientes[i][1]:
                achou = True
                index_busca = i
        if not achou:
            print("Não existe um CPF com esse nome.")
        else:
            imprimir_um_cliente(lista_clientes, index_busca)
            escolha = 0
            while escolha != 6:
                print()
                print("-----ALTERAR DADOS DO CLIENTE-----")
                print("1. Alterar nome do cliente")
                print("2. Alterar endereço do cliente")
                print("3. Alterar data de nascimento do cliente")
                print("4. Alterar telefone fixo do cliente")
                print("5. Alterar telefone celular do cliente")
                print("6. Voltar")
                escolha = int(input("Escolha uma opção: "))

                if escolha == 1:
                    lista_clientes[index_busca][0] = input("Digite o novo nome do cliente: ")
                    print()
                    print("Alteração realizada com sucesso.")
                elif escolha == 2:
                    lista_clientes[index_busca][2] = input("Digite o novo endereço do cliente: ")
                    print()
                    print("Alteração realizada com sucesso.")
                elif escolha == 3:
                    lista_clientes[index_busca][3] = input("Digite a nova data de nascimento do cliente(xx/xx/xxxx): ")
                    print()
                    print("Alteração realizada com sucesso.")
                elif escolha == 4:
                    lista_clientes[index_busca][4] = input("Digite o novo telefone fixo do cliente: ")
                    print()
                    print("Alteração realizada com sucesso.")
                elif escolha == 5:
                    lista_clientes[index_busca][5] = input("Digite o novo telefone celular do cliente: ")
                    print()
                    print("Alteração realizada com sucesso.")
                elif escolha == 6:
                    gravar_dados_cliente(lista_clientes)
                    print("Voltando e gravando dados no arquivo...")
                else:
                    opcao_invalida()



def excluir_cliente(lista_clientes):
    if len(lista_clientes) == 0:
        print()
        print("A lista de clientes está vazia.")
        print()
    else:
        busca = input("Digite o cpf do cliente para a busca: ").replace(".", "").replace("-", "")
        achou = False
        for i in range(len(lista_clientes)):
            if busca == lista_clientes[i][1]:
                achou = True
                index_busca = i
        if not achou:
            print("Não existe um CPF com esse nome.")
        else:
            imprimir_um_cliente(lista_clientes, index_busca)
            print()
            confirmar = input("Deseja excluir esse cliente?(S/N): ")
            if confirmar == 'S' or confirmar == 's':
                del lista_clientes[index_busca]
                print()
                print("Cliente excluído com sucesso.")
            else:
                print("Voltando...")



def submenu_clientes(lista_clientes):
    opcao = 0
    while opcao != 6:
        print()
        print()
        print("----------CLIENTES----------")
        print("1. Listar Todos os clientes")
        print("2. Listar um cliente")
        print("3. Incluir cliente")
        print("4. Alterar atributo do cliente")
        print("5. Excluir cliente")
        print("6. Voltar")
        opcao = int(input("Escolha uma opção: "))
        print()
        
        if opcao ==1:
            listar_todos_clientes(lista_clientes)
        elif opcao ==2:
            listar_um_cliente(lista_clientes)
        elif opcao == 3:
            incluir_cliente(lista_clientes)
        elif opcao == 4:
            alterar_cliente(lista_clientes)
        elif opcao == 5:
            excluir_cliente(lista_clientes)
        elif opcao == 6:
            gravar_dados_cliente(lista_clientes)
            print("Voltando e gravando dados no arquivo...")
        else:
            opcao_invalida()


#--------------------------------------------------------
# DAQUI PRA BAIXO É TUDO RESERVA
#--------------------------------------------------------

def incluir_reserva(lista_reservas, lista_clientes):
    if len(lista_clientes) == 0:
        print("Não é possível realizar esta ação pois não há um cliente cadastrado.")
    else:
        reserva = []
        #Código da reserva tem as limitações pois é atributo CHAVE
        código_reserva = input("Digite o código da reserva: ").replace(" ", "")
        for i in range(len(lista_reservas)):
            if código_reserva == lista_reservas[i][0]:
                print()
                print("Esse código já existe.")
                return
                
        if código_reserva not in lista_reservas:
            reserva.append(código_reserva)
        else:
            print("Verifique se o código está digitado corretamente e tente novamente.")
            return 
        
        CPF_cliente = input("Digite o CPF do cliente que irá fazer a reserva: ")
        for i in range(len(lista_clientes)):
            if CPF_cliente == lista_clientes[i][1]:
                reserva.append(CPF_cliente)
                lista_reservas.append(reserva)
                print("Reserva cadastrada com sucesso!")
                return
            
        print("Não existe um cliente com este CPF.")


def imprimir_uma_reserva(lista_reservas, indice):
    print("------------------------------------------")
    print(f"Código da reserva: {lista_reservas[indice][0]}")
    print(f"CPF: {lista_reservas[indice][1]}")
    print("------------------------------------------")



def listar_uma_reserva(lista_reservas):
    if len(lista_reservas) == 0:
        print()
        print("A lista de reservas está vazia.")
        print()
    else:
        busca = input("Digite o código da reserva para a busca: ").replace(" ", "")
        achou = False
        for i in range(len(lista_reservas)):
            if busca == lista_reservas[i][0]:
                achou = True
        if not achou:
            print("Não existe uma reserva com esse código cadastrada.")
        else:
            for i in range(len(lista_reservas)):
                if busca == lista_reservas[i][0]:
                    imprimir_uma_reserva(lista_reservas, i)



def listar_todas_reservas(lista_reservas):
    if len(lista_reservas) == 0:
        print()
        print("A lista de reservas está vazia.")
        print()
    else:
                
        print("---------------LISTA DE RESERVAS---------------")
        for i in range(len(lista_reservas)):
            print(f"Código da reserva: {lista_reservas[i][0]}")
            print(f"CPF: {lista_reservas[i][1]}")
            print("----------------------------------------------")



def excluir_reserva(lista_reservas):
    if len(lista_reservas) == 0:
        print()
        print("A lista de reservas está vazia.")
        print()
    else:
        busca = input("Digite o código da reserva para a busca: ").replace(" ", "")
        achou = False
        for i in range(len(lista_reservas)):
            if busca == lista_reservas[i][0]:
                achou = True
                index_busca = i
        if not achou:
            print("Não existe uma reserva com esse código cadastrada.")
        else:
            imprimir_uma_reserva(lista_reservas, index_busca)
            print()
            confirmar = input("Deseja excluir essa reserva?(S/N): ")
            if confirmar == 'S' or confirmar == 's':
                del lista_reservas[index_busca]
                print()
                print("Reserva excluída com sucesso.")
            else:
                print("Voltando...")



def submenu_reservas(lista_reservas, lista_clientes):
    opcao = 0
    while opcao != 6:
        print()
        print("----------RESERVAS----------")
        print("1. Listar Todas as reservas")
        print("2. Listar uma reserva")
        print("3. Incluir reserva")
        print("4. Excluir reserva")
        print("5. Voltar")
        opcao = int(input("Escolha uma opção: "))
        print()

        if opcao ==1:
            listar_todas_reservas(lista_reservas)
        elif opcao ==2:
            listar_uma_reserva(lista_reservas)
        elif opcao == 3:
            incluir_reserva(lista_reservas, lista_clientes)
        elif opcao == 4:
            excluir_reserva(lista_reservas)
        elif opcao == 5:
             print("Voltando...")
        else:
            opcao_invalida()

#--------------------------------------------------------
# DAQUI PRA BAIXO É TUDO APARTAMENTOS
#--------------------------------------------------------

def submenu_apartamentos(lista_apartamentos):
    opcao = 0
    while opcao != 6:
        print()
        print("----------APARTAMENTOS----------")
        print("1. Listar Todos os apartamentos")
        print("2. Listar um apartamento")
        print("3. Incluir apartamento")
        print("4. Alterar apartamento")
        print("5. Excluir apartamento")
        print("6. Voltar")
        opcao = int(input("Escolha uma opção: "))
        print()

        if opcao == 1:
            listar_todos_apartamentos(lista_apartamentos)
        elif opcao == 2:
            listar_um_apartamento(lista_apartamentos)
        elif opcao == 3:
            incluir_apartamento(lista_apartamentos)
        elif opcao == 4:
            alterar_apartamento(lista_apartamentos) #!!!
        elif opcao == 5:
            excluir_apartamento(lista_apartamentos) #!!!
        elif opcao == 6:
            print("Voltando...")
        else:
            opcao_invalida()

def listar_todos_apartamentos(lista_apartamentos):
    if len(lista_apartamentos) == 0:
        print()
        print("A lista de apartamentos está vazia.")
        print()
    else:
        print("LISTA DE APARTAMENTOS:")
        for i in range(len(lista_apartamentos)):
            imprimir_apartamento(lista_apartamentos, i)

def listar_um_apartamento(lista_apartamentos):
    if len(lista_apartamentos) == 0:
        print()
        print("A lista de apartamentos está vazia.")
        print()
    achou = False
    cod_buscar = input("Digite o código do apartamento que busca: ")
    for i in range (len(lista_apartamentos)):
        if cod_buscar == lista_apartamentos[i][0]:
            imprimir_apartamento(lista_apartamentos, i)
            achou = True
    if not achou:
        print()
        print("Apartamento não encontrado, tente novamente com um código existente!")

def incluir_apartamento(lista_apartamentos):
    apartamento = []

     #Código do apartamento tem as limitações pois é atributo CHAVE
    codigo_ap = input("Digite o código do apartamento (Ex: 001, 123, 999): ").replace(" ", "")
    if not codigo_ap.isdigit() or len(codigo_ap) != 3:
        opcao_invalida()
        return
    else:
        if len(lista_apartamentos) > 0:
            for i in range (len(lista_apartamentos)):
                if codigo_ap == lista_apartamentos[i][0]:
                    print()
                    print("Esse código de apartamento já está cadastrado, tente novamente com outro")
                    return
        apartamento.append(codigo_ap)
    
    descricao = input("Digite a descrição do apartamento: ")
    apartamento.append(descricao)

    num_adultos = int(input("Digite o número de adultos: "))
    apartamento.append(num_adultos)

    num_criancas = int(input("Digite o número de crianças: "))
    apartamento.append(num_criancas)

    valor = input("Digite o valor da diária do apartamento (Ex: 349,99 ; 500,00 ; 1000,50): ")
    apartamento.append(valor)

    lista_apartamentos.append(apartamento)
    print()
    print("Apartamento adicionado com sucesso.")
    #ÍNDICES APARTAMENTO:
    #0 - CÓDIGO; 1 - DESCRIÇÃO; 2 - NÚMERO DE ADULTOS; 3 - NÚMERO DE CRIANÇAS; 4 - VALOR.

def alterar_apartamento(lista_apartamentos):
    print()
    if len(lista_apartamentos) == 0:
        print()
        print("A lista de apartamentos está vazia.")
        print()
    cod_buscar = input("Digite o código do apartamento que deseja alterar atributos: ")
    achou = False
    n = 0
    for i in range(len(lista_apartamentos)):
        if cod_buscar == lista_apartamentos[i][0]:
            achou = True
            imprimir_apartamento(lista_apartamentos, i)
            while n != 5:
                print()
                print("-----ALTERAR DADOS DO APARTAMENTO-----")
                print("1. Alterar descrição")
                print("2. Alterar número de adultos")
                print("3. Alterar número de crianças")
                print("4. Alterar valor")
                print("5. Voltar")
                n = int(input("Escolha uma opção: "))

                if n == 1:
                    lista_apartamentos[i][1] = input("Altere a descrição do apartamento: ")
                    print("Atributo alterado com sucesso.")
                
                elif n == 2:
                    lista_apartamentos[i][2] = input("Altere o número de adultos do apartamento: ")
                    print("Atributo alterado com sucesso.")

                elif n == 3:
                    lista_apartamentos[i][3] = input("Altere o número de crianças do apartamento: ")
                    print("Atributo alterado com sucesso.")

                elif n == 4:
                    lista_apartamentos[i][4] = input("Altere o valor do apartamento: ")
                    print("Atributo alterado com sucesso.")

                elif n == 5:
                    print("Voltando...")

                else:
                    opcao_invalida()
    if not achou:
        print("Apartamento não encontrado.")
    

def excluir_apartamento(lista_apartamentos):
    cod_buscar = input("Digite o código do apartamento que deseja excluir: ")
    achou = False
    for i in range(len(lista_apartamentos)):
        if cod_buscar == lista_apartamentos[i][0]:
            achou = True
            imprimir_apartamento(lista_apartamentos, i)
            while achou == True:
                confirm = input("Deseja excluir este apartamento? (S/N): ")
                if confirm.upper() == "S":
                    del lista_apartamentos[i]
                    print("Apartamento excluído com sucesso.")
                    return
                elif confirm.upper() == "N":
                    print("Voltando...")
                    return
                else:
                    opcao_invalida()
    if not achou:
        print("Apartamento não encontrado.")


def imprimir_apartamento(lista_apartamentos, i):
    print(f"---------------APARTAMENTO #{lista_apartamentos[i][0]}---------------")
    print(f"Descrição: {lista_apartamentos[i][1]}")
    print(f"Número de adultos: {lista_apartamentos[i][2]}")
    print(f"Número de crianças: {lista_apartamentos[i][3]}")
    print(f"Valor: {lista_apartamentos[i][4]}")
    print("----------------------------------------------")
    
#ARQUIVOS APARTAMENTOS



#--------------------------------------------------------
#DAQUI PRA BAIXO É TUDO RESERVA DE APARTAMENTOS
#--------------------------------------------------------

def submenu_reserva_apartamentos():
    opcao = 0
    while opcao != 6:
        print()
        print("----------RESERVAS DE APARTAMENTOS----------")
        print("1. Listar Todos as reservas de apartamentos")
        print("2. Listar uma reserva de apartamento")
        print("3. Incluir reserva de apartamento")
        print("4. Alterar reserva de apartamento")
        print("5. Excluir reserva de apartamento")
        print("6. Voltar")
        opcao = int(input("Escolha uma opção: "))
        print()



def opcao_invalida():
    print()
    print("-------------------------")
    print("Digite uma opção válida.")
    print("-------------------------")
    
    

def menu():
    opcao = 0
    clientes = []
    apartamentos = []
    reservas = []
    if existe_arquivo("Clientes.txt"):
        carregar_dados_arquivos_cliente(clientes)
    else:
        gravar_dados_cliente("Clientes.txt")

    while opcao != 6:
        print()
        print("----------MENU PRINCIPAL---------")
        print("1. Submenu de Clientes")
        print("2. Submenu de Reservas")
        print("3. Submenu de Apartamentos")
        print("4. Submenu de Reservas de Apartamentos")
        print("5. Submenu Relatórios")
        print("6. Sair")
        opcao = int(input("Escolha uma opção: "))
        
        if opcao == 1:
            submenu_clientes(clientes)

        elif opcao == 2:
            submenu_reservas(reservas, clientes)

        elif opcao == 3:
            submenu_apartamentos(apartamentos)
            #carregar_dados_arquivos(apartamentos, "Apartamentos.txt")

        elif opcao == 4:
            submenu_reserva_apartamentos()

        elif opcao == 5:
            print("opçao 5")

        elif opcao == 6:
            print("Saindo...")
        
        else:
            opcao_invalida()


'''-----OBS-----
PARA OS ARQUIVOS, DEVE-SE SOBRESCREVER O ARQUIVO REFERENTE DA VARIAVEL
AO SAIR DO SUBMENU REFERENTE A ELE
ex: entrou no submenu de clientes, ele vai sobrescrever os dados no arquivo
só quando sair desse submenu de clientes.'''

def main():
    menu()


main()

'''
TENTANDO GENERALIZAR A FUNÇÃO DE CARREGAR ARQUIVO, AINDA NÃO ESTÁ FUNCIONANDO!!!!
def carregar_dados_arquivos(lista, arq):
    if existe_arquivo(arq):
        arquivo = open(arq, 'r', encoding="utf-8")
        for linha in arquivo:
            linha = linha[:(len(linha)-1)]
            linha = linha.split(";")
            lista.append(linha)
        arq.close()
'''