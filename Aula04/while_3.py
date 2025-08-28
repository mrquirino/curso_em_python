# Este código soicita ao usuário uma resposta e continua executando
# enquanto a resposta for "sim"
resposta = input("Deseja continuar? (digite 'sim' para continuar): ")

# A função lower() transforma toda a string em letras minúsculas
while resposta.lower() == "sim":
    resposta = input("Deseja continuar? (digite 'sim' para continuar): ")