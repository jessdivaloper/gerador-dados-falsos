import csv
import random
from faker import Faker

# Inicializa o gerador de dados fictícios
faker = Faker('pt_BR')

# Nome do arquivo CSV
nome_arquivo = 'alunos.csv'

# Gera 300 alunos
with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as arquivo_csv:
    escritor = csv.writer(arquivo_csv)

    # Cabeçalho
    escritor.writerow(['matricula', 'nome_aluno', 'id_curso', 'data_nascimento', 'endereco', 'status'])

    for i in range(1, 301):
        matricula = f"MAT{i:04d}"
        nome_aluno = faker.name()
        id_curso = random.randint(1, 10)
        data_nascimento = faker.date_of_birth(minimum_age=18, maximum_age=40).strftime('%Y-%m-%d')
        endereco = faker.address().replace("\n", ", ")
        status = random.choice(['ativo', 'inativo'])

        escritor.writerow([matricula, nome_aluno, id_curso, data_nascimento, endereco, status])

print(f"Arquivo '{nome_arquivo}' gerado com sucesso.")
