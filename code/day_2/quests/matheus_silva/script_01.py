#1 - Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

v = []
i = 0 
while i < 5:
    print("Digite o valor ", i + 1 )
    num = int(input())
    v.append(num)
    i = i + 1

print(v)