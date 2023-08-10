"""
7 - Faça um Programa que verifique se uma letra digitada é "F" 
ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

"""

print("Digite o Sexo (F/M):")
genero = input()
if genero.upper() == "F":
    print("F - Feminino")
elif genero.upper() == "M":
    print("M - Masculino")
else:
        print("Sexo Inválido.")

