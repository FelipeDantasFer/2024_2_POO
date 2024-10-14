nome = input("Digite seu nome: ")
salarioF = float(input("Informe o salario: "))
totalVendas = float(input("Informe o total de vendas: "))
comissao = (totalVendas * 0.15) + salarioF
print(f"TOTAL = R$ {comissao:.2f}")