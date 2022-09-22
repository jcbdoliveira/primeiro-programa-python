opcao = '-1'

while opcao != '0':
    opcao = input("informe a opção: \n [1]Sacar \n [2]Despósito \n") 

    if opcao == '1':
        print("sacando")
    elif opcao == '2':
        print("depósito")   

    if opcao == '0':
        print("saindo")
        break

print("Obrigado por utilizar nosso banco.")

while True:
    numero = input("informe um número: ") 

    if numero == '10':
        print("saindo")
        break
    
    print(numero)
