print("Digite o número correspondente ao mês:")
print("""1 - Janeiro
      2 - Fevereiro 
      3 - Março 
      4 - Abril 
      5 - Maio 
      6 - Junho 
      7 - Julho 
      8 - Agosto 
      9 - Setembro 
      10 - Outubro 
      11 - Novembro 
      12 - Dezembro """)

try:
    numero = int(input("Sua escolha: "))
                     
match numero:
       case 1:
            mes = "Janeiro"
        case 2:
            mes = "Fevereiro"
        case 3:
            mes = "Março"
        case 4:
            mes = "Abril"
        case 5:
            mes = "Maio"
        case 6:
            mes = "Junho"
        case 7:
            mes = "Julho"
        case 8:
            mes = "Agosto"
        case 9:
            mes = "Setembro"
        case 10:
            mes = "Outubro"
        case 11:
            mes = "Novembro"
        case 12:
            mes = "Dezembro"
        case _:
            print("Mês inválido")
except ValueError:
    print("Você não digitou um número")
    
print("O mês selecionador é: ", mes)
            
