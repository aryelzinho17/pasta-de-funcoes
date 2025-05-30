def mostra_linha():
    """"
    mostra uma linha de separaçao
    """
    print('-' * 50)

# exemplo de uso de funçao mostra_linha
mostra_linha()   

print("aluguel de carros com a maior frota do brasil | localiza")

mostra_linha()

print("seja bem vindo")

mostra_linha()

nome = input("Digite seu nome")

print(f"ola,{nome} Estamos felizes em te-lo conosco.")

mostra_linha()

print("selecione o carro que deseja alugar:")
print("1 - bmw ")
print("2 - mustang ")
print("3 - hb20 ")
print("4 - fusca ")
print("5 - civic")
print("0 - sair ")

carro = int(input("digite o carro que desejar alugar"))

match carro:
    case 1:
        print("carro: bmw - preço: R$ 1.143.950")
    case 2:
        print("carro: mustang - preço: R$ 1.146.650")  
    case 3:
        print("carro: hb20 - preço: R$ 1.145.120") 
    case 4:
        print("carro: fusca - preço: R$ 1.148.123")  
    case 5:
        print("carro: civic - preço: R$ 1.142.000") 
    case 0:
        print("saindo do programa...")
        exit() # encerra o programa se o codigo for 0
    case _:
        pront("codigo invalido. por favor, selecione um codigo do menu")