alunos = {}

nomes = ["Ana", "Carlos", "Bianca", "Felipe"]

for nome in nomes:
    idade = input(f"Digite a idade de {nome}: ") # Entrada de idade
    alunos[nome] = idade # Adiciona ao dicionário

# Exibe a lista alunos com sua idades
print("\nLista de alunos: ")
print()
for nome, idade in alunos.items():
    print(f"{nome}: {idade} anos")

print()
input("Presione alguma tecla para sair...")