salario_contribuinte = float(input("Digite o salário: "))

if salario_contribuinte <= 1693.72:
    contribuicao_inss = salario_contribuinte * 0.08

elif salario_contribuinte <= 2822.90:
    contribuicao_inss = salario_contribuinte * 0.09

elif salario_contribuinte <= 5645.90:
    contribuicao_inss = salario_contribuinte * 0.11

else:
    contribuicao_inss = 621.03  # Valor fixo do teto do INSS

salario_liquido = salario_contribuinte - contribuicao_inss

print(f"Sua contribuição é: R$ {contribuicao_inss:.2f}")
print(f"O salário bruto é: R$ {salario_contribuinte:.2f}")
print(f"O salário líquido é: R$ {salario_liquido:.2f}")
