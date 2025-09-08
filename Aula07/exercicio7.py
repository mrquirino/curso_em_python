Aluno1 = ("João", 11, "5º Ano")
Aluno2 = ("Maria", 13, "7º Ano")
Aluno3 = ("Pedro", 14, "8º Ano")

notas_alunos1 = (8.5, 7.0, 9.0, 6.5)
notas_alunos2 = (9.0, 8.5, 7.5, 10.0)
notas_alunos3 = (6.0, 7.5, 8.0, 9.0)

nome1, idade1, turma1 = Aluno1
print("Nome: {nome1}, Idade: {idade1}, Profissão: {turma1}")

nome2, idade2, turma2 = Aluno2
print("Nome: {nome2}, Idade: {idade2}, Profissão: {turma2}")

nome3, idade3, turma3 = Aluno3
print("Nome: {nome3}, Idade: {idade3}, Profissão: {turma3}")

nota1_1, nota1_2, nota1_3, nota1_4 = notas_alunos1
print(f"Notas de {nome1}: {nota1_1}, {nota1_2}, {nota1_3}, {nota1_4}")

nota2_1, nota2_2, nota2_3, nota2_4 = notas_alunos2
print(f"Notas de {nome2}: {nota2_1}, {nota2_2}, {nota2_3}, {nota2_4}")

nota3_1, nota3_2, nota3_3, nota3_4 = notas_alunos3
print(f"Notas de {nome3}: {nota3_1}, {nota3_2}, {nota3_3}, {nota3_4}")

# Menor nota do Aluno 1
print(min(notas_alunos1))

# Maior nota do Aluno 2
print(max(notas_alunos2))

# Soma das notas do Aluno 3
print(sum(notas_alunos3))