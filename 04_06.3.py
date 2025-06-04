import re

def validar_email(email_str):
    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z"
    return re.match(email_regex, email_str) is not None

print("---- Validador de E-mail ----")
while True:
    email_digitando = input("Digite seu e-mail (ou 'sair' para sair): ")
    if email_digitando.lower() == 'sair':
        print("Encerrando o programa.")
        break
    
    if validar_email(email_digitando):
        print(f"'{email_digitado}' é um email válido.")
    else:
        print(f"'{email_digitado}' é um email inválido.")
        print("-" * 30)