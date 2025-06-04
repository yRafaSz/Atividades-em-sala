import re

def validar_nome(nome):
    padrao = "^[a-zA-Z]+$"
    if re.match(padrao, nome):
        return True
    else:
        return False
    
def validar_idade(idade):
    padrao = "^[0-9]+&"
    if re.match(padrao, idade):
        return True
    else:
        return False
    
nome = input("Digite seu nome: ")
print()
idade = input("Digite sua idade: ")

print("Seu nome: ", nome)
print("Sua idade: ", idade)
print()
if validar_nome(nome) and validar_idade(idade):
    print("Seu nome e idade estão corretos!")
else:
    print("Seus dados são inválidos")
    
print()
input("Pressione uma tecla para sair...")