#--------------------------------------------------------
#DAQUI PRA BAIXO SÃO FUNÇÕES GERAIS
#--------------------------------------------------------

def procurar(lista, código_chave, indice_na_lista):
    achou = False
    for i in range(len(lista)):
        if busca == lista[i][0]:

            return i

    print("Não existe uma informação cadastrada com esse código.")
    return False



#colocar esse na linha 339 ou próximo
else:
    busca = input("Digite o código da reserva para a busca: ").replace(" ", "")
    index_busca = procurar(lista_reservas, busca, 0)

    imprimir_uma_reserva(lista_reservas, index_busca)
    print()
    confirmar = input("Deseja excluir essa reserva?(S/N): ")
    if confirmar == 'S' or confirmar == 's':
        del lista_reservas[index_busca]
        print()
        print("Reserva excluída com sucesso.")
    else:
        print("Voltando...")






#RESTRIÇÃO PARA INCLUIR UM APARTAMENTO JÁ RESERVADO
        if len(lista_reservas_apartamentos) > 0:
            for i in range (len(lista_reservas_apartamentos)):
                if cod_apto == lista_reservas_apartamentos[i][1]:
                    print()
                    print("Esse código já está cadastrado em uma reserva de apartamento, tente novamente com outro")
                    return