def aumento (percentual, salario):
   return (percentual / 100) * salario

def salariofinal(valoraumento, salario):
   return (valoraumento + salario)

salario = float(input("Digite seu salário inicial  ""R$"))
percentual = float(input("Qual será seu percentual de aumento? "))

valoraumento = aumento(percentual, salario)
valorfinal = salariofinal(valoraumento , salario)

print("O valor do seu aumento salarial referente ao seu salario atual será de : ", valoraumento)
print("O valor final do seu salario será de: ", valorfinal)
