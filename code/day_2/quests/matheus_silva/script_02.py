"""
2 - Faça um Programa que peça a idade e a altura de 5 pessoas, 
armazene cada informação no seu respectivo vetor. Imprima a idade e a 
altura na ordem inversa a ordem lida.

"""
idades = []
alturas = []
i=0
while i < 5:
    print("Digite a idade da pessoa", i + 1 )
    idade = int(input())
    print("Digite a altura da pessoa", i + 1 )
    altura = float(input())
    idades.append(idade)
    alturas.append(altura)
    i = i + 1

j = 4

while j>=0:
    print("A idade da pessoa", j + 1, "eh", idades[j], "e sua altura eh", alturas[j], "m")
    j = j - 1