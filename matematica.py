while True:
    print("Menu:")
    print("1. Soma")
    print("2. Multiplicação")
    print("3. Subtração")
    print("4. Sair")
    escolha = input ("Escolha uma opção:")
    if escolha == "1":
       num1 = float (input("escolha um numero:"))
       num2 = float (input ("escolha um numero:"))
       resultado = num1 + num2
       print(resultado)
       pass
    elif escolha =="2":
       num3 = float (input("escolha um numero:"))
       num4 = float (input ("escolha um numero:"))
       resultado = num3 * num4
       print(resultado)
       pass
    elif escolha =="3":
       num5 = float (input("escolha um numero:"))
       num6 = float (input ("escolha um numero:"))
       resultado = num5 - num6
       print(resultado)
       pass
    elif escolha =="4":
       break
    else: 
       print("Opção inválida. Tente novamente")
