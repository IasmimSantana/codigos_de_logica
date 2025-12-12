Funcionario= input("Entre com o cargo:")
Dia= input("Entre com o dia:")

if (Funcionario == "Gerente" or Funcionario == "Estagiario") and (Dia == "Segunda" or Dia == "Quinta"):
    print("Acesso liberado")
else:
    print("Acesso negado")

