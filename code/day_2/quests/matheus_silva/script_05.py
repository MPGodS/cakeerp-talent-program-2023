"""
5 - Faça um programa com uma função chamada somaImposto. 
A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em
porcentagem e custo, que é o custo de um item antes do imposto. A função “altera” o valor de custo para 
incluir o imposto sobre vendas.

"""
def somaImposto(taxaImposto, custo):
    return custo + (custo * (taxaImposto/100))

print("Digite o valor do produto")
custo = int(input())
print("Digite o valor da taxa de imposto em porcentagem: ex: 17")
imposto = int(input())

print("O valor final do produto eh R$", somaImposto(imposto,custo))
