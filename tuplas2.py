frutas = ("Maçã", "Banana", "Cereja")

# Exibindo a topia
print("Minha tupla de frutas:", frutas)

#Acessando elementos da tupla pelo índice
print("Primeira fruta:", frutas[0])
print("Segunda fruta:", frutas[1])
print("Terceira fruta:", frutas[2])

# Tentando modificar um elemento da tupla ( isso gerará um erro )

# Descobrindo o tamanho da tupla
print("Número de frutas na tupla:", len(frutas))

# Percorrendo a tupla com um loop
print("Listando todas as frutas na tupla:")
for fruta in frutas:
    print(fruta)

# Verificando se um elemento está na tupla
if 'banana' in frutas:
    print("Banana está na tupla")

# Criando uma tupla de um único elemento ( note e vírgula no final )
unica_final = ("melancia",)
print("Tupla de um único elemento:", unica_final)