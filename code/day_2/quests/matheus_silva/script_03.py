"""
3 - Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
A. "Telefonou para a vítima?"
B. "Esteve no local do crime?"
C. "Mora perto da vítima?"
D. "Devia para a vítima?"
E. "Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada
como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

"""
perguntas = ["Telefonou para a vítima?",
             "Esteve no local do crime?",
             "Mora perto da vítima?",
             "Devia para a vítima?",
             "Já trabalhou com a vítima?"]

respostas = []

i=0

while i < 5:
    print(perguntas[i])
    print("Responda apenas com sim ou nao!")
    resposta = input()
    respostas.append(resposta.lower())
    i = i + 1

numero_de_respostas = respostas.count("sim")
print(numero_de_respostas)

if numero_de_respostas == 2:
    print("Suspeita!")
elif numero_de_respostas >= 3 and numero_de_respostas<=4:
    print("Cumplice!")
elif numero_de_respostas == 5:
    print("Assasino!!")
else: 
    print("Inocente")