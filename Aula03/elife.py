# Solicitar os anos de experiência doprofissional
anos_experiencia = int(input("Digite quantos anos de experiência o profissional possui: "))

# Verificar a classificação do profissional com base nos anos de experiência
if anos_experiencia < 5:
    print("Profissional em início de carreira - Júnior")
elif anos_experiencia >= 5 and anos_experiencia < 10:
    print("Profissional Pleno")
elif anos_experiencia >= 10 and anos_experiencia < 15:
    print("Profissional Sênior")
else:
    print("Profissional Master")