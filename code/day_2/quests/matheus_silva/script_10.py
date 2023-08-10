"""
10 - As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores 
e lhe contraram para desenvolver o programa que
calculará os reajustes. Faça um programa que recebe o salário de um colaborador e o reajuste 
segundo o seguinte critério, baseado no salário
atual:

A. salários até R$ 280,00 (incluindo) : aumento de 20%
B. salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
C. salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
D. salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
E. o salário antes do reajuste;
F. o percentual de aumento aplicado;
G. o valor do aumento;
H. o novo salário, após o aumento.

"""
def porcentagem_de_reajuste(salario_atual):
    if salario_atual <= 280:
        percentual = 20
    elif salario_atual <= 700:
        percentual = 15
    elif salario_atual <= 1500:
        percentual = 10
    else:
        percentual = 5
    return percentual

print("Digite o valor do salario atual:")
salario_atual = float(input())
percentual = porcentagem_de_reajuste(salario_atual)

print("salario antes do reajuste: R$", salario_atual)
print("O percentual de aumento será:", percentual, "%")
print("O valor do aumento vai ser R$", salario_atual*(percentual/100))
print("O novo salario é: R$",salario_atual+(salario_atual * (percentual/100)))
