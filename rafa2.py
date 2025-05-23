def pagamento(horas_trabalhadas, valor_hora):
    valor_pago = horas_trabalhadas + valor_hora
    return valor_pago
print("Digite o número de horas trabalhadas: ")
horas_trabalhadas = float(input())

print("Digite o valor da hora de trabalho: ")
valor_hora = float(input())

valor_a_pagar = pagamento(horas_trabalhadas, valor_hora)
print("O valor a ser pago é:", valor_a_pagar)