"""
9 - Faça um Programa que leia três números e mostre-os em ordem decrescente.
"""
numeros=[]
i =0
while i <3:
    print("Digite o valor ", i + 1)
    num = int(input())
    numeros.append(num)
    i = i + 1
    
print(sorted(numeros))