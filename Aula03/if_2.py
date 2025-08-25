# Solicitar a nota do aluno em uma disciplina
nota = float(input("Digite a nota do aluno: "))

# Verificar a situação do aluno com base na nota
if nota >= 9.0:
    print("Conceito A - Excelente")
if nota >= 7.0 and nota < 9.0:
    print("Conceito B - Bom")
if nota >= 5.0 and nota < 7.0:
    print("Conceito C - Regular")
if nota < 5.0:
    print("Conceito D - Insuficiente")