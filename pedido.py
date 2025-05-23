print("      Pizzaria KomeBen - Ltda")
print(" -_-_-_-_Cardápio do local-_-_-_-_")
print(" ")
print(" ----- Sabores: -----")
print(" Calabresa, Frango e Catupiry")
print ("")
print("******Pizzas - Tamanhos******")
print ("")
print(" Pizza pequena -      R$: 14,99")
print(" Pizza média -        R$: 19,99")
print(" Piza grande -        R$: 24,99")
print ("")
print("Opções de Refrigerante(s)")
print ("")
print(" Coca-cola -      R$: 6,99")
print(" Guaraná -        R$: 5,99")
print(" Fanta ( uva ) -  R$: 4,99")
print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")
print(" ")

print(" Escolha o sabor da sua Pizza: ")
print(" ")
print("1 - Calabresa ")
print("2 - Frango ")
print("3 - Catupiry ")
pedidopizza = input()

print(" Informe o tamanho da Pizza: ")
print(" ")
print("P - Pequena ")
print("M - Média ")
print("G - Grande ")
print(" ")
tampizza = input().upper()

print(" Escolha sua bebida: ")
print(" ")
print("1 - Coca-Cola ")
print("2 - Guaraná ")
print("3 - Fanta Uva ")
print(" ")
pedidorefri = input()

# Pizza Calabresa
if (pedidopizza == "1") and (tampizza == "P") and (pedidorefri == "1"):
    precopagar = 14.99 + 6.99
    pedidos = "Calabresa, pequena, Coca-Cola"
elif (pedidopizza == "1") and (tampizza == "P") and (pedidorefri == "2"):
    precopagar = 14.99 + 5.99
    pedidos = "Calabresa, pequena, Guaraná"
elif (pedidopizza == "1") and (tampizza == "P") and (pedidorefri == "3"):
    precopagar = 14.99 + 4.99
    pedidos = "Calabresa, pequena, Fanta"

elif (pedidopizza == "1") and (tampizza == "M") and (pedidorefri == "1"):
    precopagar = 19.99 + 6.99
    pedidos = "Calabresa, média, Coca-Cola"
elif (pedidopizza == "1") and (tampizza == "M") and (pedidorefri == "2"):
    precopagar = 19.99 + 5.99
    pedidos = "Calabresa, média, Guaraná"
elif (pedidopizza == "1") and (tampizza == "M") and (pedidorefri == "3"):
    precopagar = 19.99 + 4.99
    pedidos = "Calabresa, média, Fanta"

elif (pedidopizza == "1") and (tampizza == "G") and (pedidorefri == "1"):
    precopagar = 24.99 + 6.99
    pedidos = "Calabresa, grande, Coca-Cola"
elif (pedidopizza == "1") and (tampizza == "G") and (pedidorefri == "2"):
    precopagar = 24.99 + 5.99
    pedidos = "Calabresa, grande, Guaraná"
elif (pedidopizza == "1") and (tampizza == "G") and (pedidorefri == "3"):
    precopagar = 24.99 + 4.99
    pedidos = "Calabresa, grande, Fanta"

# Pizza Frango
elif (pedidopizza == "2") and (tampizza == "P") and (pedidorefri == "1"):
    precopagar = 14.99 + 6.99
    pedidos = "Frango, pequena, Coca-Cola"
elif (pedidopizza == "2") and (tampizza == "P") and (pedidorefri == "2"):
    precopagar = 14.99 + 5.99
    pedidos = "Frango, pequena, Guaraná"
elif (pedidopizza == "2") and (tampizza == "P") and (pedidorefri == "3"):
    precopagar = 14.99 + 4.99
    pedidos = "Frango, pequena, Fanta"

elif (pedidopizza == "2") and (tampizza == "M") and (pedidorefri == "1"):
    precopagar = 19.99 + 6.99
    pedidos = "Frango, média, Coca-Cola"
elif (pedidopizza == "2") and (tampizza == "M") and (pedidorefri == "2"):
    precopagar = 19.99 + 5.99
    pedidos = "Frango, média, Guaraná"
elif (pedidopizza == "2") and (tampizza == "M") and (pedidorefri == "3"):
    precopagar = 19.99 + 4.99
    pedidos = "Frango, média, Fanta"

elif (pedidopizza == "2") and (tampizza == "G") and (pedidorefri == "1"):
    precopagar = 24.99 + 6.99
    pedidos = "Frango, grande, Coca-Cola"
elif (pedidopizza == "2") and (tampizza == "G") and (pedidorefri == "2"):
    precopagar = 24.99 + 5.99
    pedidos = "Frango, grande, Guaraná"
elif (pedidopizza == "2") and (tampizza == "G") and (pedidorefri == "3"):
    precopagar = 24.99 + 4.99
    pedidos = "Frango, grande, Fanta"

# Pizza Catupiry
elif (pedidopizza == "3") and (tampizza == "P") and (pedidorefri == "1"):
    precopagar = 14.99 + 6.99
    pedidos = "Catupiry, pequena, Coca-Cola"
elif (pedidopizza == "3") and (tampizza == "P") and (pedidorefri == "2"):
    precopagar = 14.99 + 5.99
    pedidos = "Catupiry, pequena, Guaraná"
elif (pedidopizza == "3") and (tampizza == "P") and (pedidorefri == "3"):
    precopagar = 14.99 + 4.99
    pedidos = "Catupiry, pequena, Fanta"

elif (pedidopizza == "3") and (tampizza == "M") and (pedidorefri == "1"):
    precopagar = 19.99 + 6.99
    pedidos = "Catupiry, média, Coca-Cola"
elif (pedidopizza == "3") and (tampizza == "M") and (pedidorefri == "2"):
    precopagar = 19.99 + 5.99
    pedidos = "Catupiry, média, Guaraná"
elif (pedidopizza == "3") and (tampizza == "M") and (pedidorefri == "3"):
    precopagar = 19.99 + 4.99
    pedidos = "Catupiry, média, Fanta"

elif (pedidopizza == "3") and (tampizza == "G") and (pedidorefri == "1"):
    precopagar = 24.99 + 6.99
    pedidos = "Catupiry, grande, Coca-Cola"
elif (pedidopizza == "3") and (tampizza == "G") and (pedidorefri == "2"):
    precopagar = 24.99 + 5.99
    pedidos = "Catupiry, grande, Guaraná"
elif (pedidopizza == "3") and (tampizza == "G") and (pedidorefri == "3"):
    precopagar = 24.99 + 4.99
    pedidos = "Catupiry, grande, Fanta"

else:
    precopagar = 0.0
    pedidos = "Pedido inválido!"

print(" Nota fiscal - KomeBen")
print("")
print(f"Seus pedidos: {pedidos} - R$: {precopagar:.2f}")
print("")
print("Volte sempre! Qualquer dúvida ou problema nos informe.")
print("Endereço: rua 3 - Ribeirão das Neves 45")
print("")
input("Pressione Enter para sair...")
