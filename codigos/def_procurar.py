#--------------------------------------------------------
#DAQUI PRA BAIXO SÃO FUNÇÕES GERAIS
#--------------------------------------------------------

def procurar(lista, código_chave):
    achou = False
    for i in range(len(lista)):
        if busca == lista[i][0]:
            achou = True
            return i

    print("Não existe uma informação cadastrada com esse código.")
    return



#colocar esse na linha 339 ou próximo
else:
    busca = input("Digite o código da reserva para a busca: ").replace(" ", "")
    index_busca = procurar(lista_reservas, busca)

    imprimir_uma_reserva(lista_reservas, index_busca)
    print()
    confirmar = input("Deseja excluir essa reserva?(S/N): ")
    if confirmar == 'S' or confirmar == 's':
        del lista_reservas[index_busca]
        print()
        print("Reserva excluída com sucesso.")
    else:
        print("Voltando...")