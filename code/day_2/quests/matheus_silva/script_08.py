# coding: utf-8
"""
8 - Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular
 a média alcançada por aluno e apresentar:
A. A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
B. A mensagem "Reprovado", se a média for menor do que sete;
C. A mensagem "Aprovado com Distinção", se a média for igual a dez.

"""

def media_das_notas(nota1, nota2):
    return (nota1 + nota2)/2

print("Digite o valor da nota 1")
num1 = int(input())
print("Digite o valor da nota 2")
num2 = int(input())

media = media_das_notas(num1, num2)

if media == 10:
    print("Aprovado com Distinção")
elif media >= 7:
    print("Aprovado")
else:
       print("Reprovado") 