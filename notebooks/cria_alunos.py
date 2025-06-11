import csv
import random

nomes = [
    "Ana Silva", "Bruno Souza", "Carla Oliveira", "Daniel Santos", "Eduarda Lima",
    "Felipe Costa", "Gabriela Rocha", "Henrique Alves", "Isabela Martins", "João Pereira",
    "Karina Dias", "Lucas Fernandes", "Mariana Ribeiro", "Nicolas Teixeira", "Olivia Barros",
    "Paulo Mendes", "Quésia Farias", "Rafael Gomes", "Sofia Cardoso", "Tiago Moreira"
]

with open('alunos.csv', mode='w', newline='', encoding='utf-8') as arquivo:
    writer = csv.writer(arquivo)
    writer.writerow(['matricula', 'nome_aluno', 'id_curso'])
    for i, nome in enumerate(nomes, start=1):
        matricula = f"{2024000 + i}"
        id_curso = random.randint(1, 10)
        writer.writerow([matricula, nome, id_curso])