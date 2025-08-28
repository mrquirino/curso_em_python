# Exemplo de maior (>)
# O loop continuará enquanto o valor digitado for menor que 10
entrada = int(input("Digite um número maior que 10 para continuar: "))
while entrada > 10:
    entrada = int(input("Digite novamente: "))

# Exemplo de menor (<)
# O loop continuará enquanto o valor digitado for menor que 5
entrada = int(input("Digite um número menor que 5 para continuar: "))
while entrada < 5:
    entrada = int(input("Digite novamente: "))

# Exemplo de igual (==)
# O loop continuará enquanto o valor digitado for igual a 3
entrada = int(input("Digite o número 3 para continuar: "))
while entrada == 3:
        entrada = int(input("Digite novamente: "))

# Exemplo de maior ou igual (>=)
# O loop continuará enquanto o valor digitado for maior ou igual a 7
entrada = int(input("Digite um número maior ou igual a 7 para continuar: "))
while entrada >= 7:
    entrada = int(input("Digite novamente: "))

# Exemplo de menor ou igual (<=)
# O loop continuará enquanto o valor digitado for menor ou igual a 2
entrada = int(input("Digite um número menor ou igual a 2 para continuar: "))
while entrada <=2:
    entrada = int(input("Digite novamente: "))

# Exemplo de diferente (!=)
# O loop continuará enquanto o valor digitado for diferente de 0
entrada = int(input("Digite qualuqer número diferente de 0 para continuar: "))
while entrada != 0:
    entrada = int(input("Digite novamnete: "))

# Entrda de igualdade de valor e tipo (===)
# Em Python, não existe o operador '===',
# então usaremos o operador '==' para comparar o valor e tipo
# O loop continuará enquanto o valor digitado for exatamente igual (mesmo tipo e valor) a "sair"
entrada = input("Digite 'sair' para encerrar: ")
while entrada == "sair":
    entrada = input("Digite novamente: ")