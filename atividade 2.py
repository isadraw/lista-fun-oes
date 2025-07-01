def valor(preco , desconto):
    return (desconto/100) * preco

def valor2(preco , valordesconto):
    return preco - valordesconto

preco = float(input("Digite o valor inicial da mercadoria"))
desconto = float(input("digite o percentual de desconto, ex: 50 , 40 , 45"))

valordesconto = valor(preco , desconto)
valorfinal = valor2(preco , valordesconto)

print("o valor do desconto será de", valordesconto)
print("O valor final do produto será de", valorfinal)