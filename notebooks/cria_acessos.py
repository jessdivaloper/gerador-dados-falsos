import csv
import random
from datetime import datetime, timedelta

# Gera uma lista de 300 matrículas
matriculas = [f'MAT{str(i).zfill(4)}' for i in range(1, 301)]

# Função para gerar timestamp de acesso e tempo de duração
def gerar_acesso():
    # Gera um datetime entre 1º de janeiro e 31 de maio de 2024
    data_base = datetime.strptime('2024-01-01', '%Y-%m-%d')
    data_acesso = data_base + timedelta(days=random.randint(0, 150), hours=random.randint(7, 22), minutes=random.randint(0, 59))
    tempo_duracao = random.randint(5, 180)  # tempo em minutos
    return data_acesso.strftime('%Y-%m-%d %H:%M:%S'), tempo_duracao

# Criar e escrever no CSV
with open('acessos_alunos.csv', mode='w', newline='', encoding='utf-8') as arquivo_csv:
    escritor = csv.writer(arquivo_csv)
    escritor.writerow(['matricula', 'timestamp_acesso', 'tempo_duracao_min'])

    for matricula in matriculas:
        num_acessos = random.randint(3, 10)
        for _ in range(num_acessos):
            timestamp, duracao = gerar_acesso()
            escritor.writerow([matricula, timestamp, duracao])

print("Arquivo 'acessos_alunos.csv' gerado com sucesso.")
# O código acima gera um arquivo CSV com acessos de alunos, contendo matrículas, timestamps e duração dos acessos.