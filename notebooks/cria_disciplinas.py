import csv
import random

# Cursos fornecidos
cursos = {
    1: 'Engenharia de Computação',
    2: 'Administração',
    3: 'Direito',
    4: 'Medicina',
    5: 'Psicologia',
    6: 'Engenharia Civil',
    7: 'Ciências Contábeis',
    8: 'Arquitetura e Urbanismo',
    9: 'Enfermagem',
    10: 'Publicidade e Propaganda'
}

# Disciplinas por curso
disciplinas_por_curso = {
    1: ['Algoritmos', 'Estrutura de Dados', 'Sistemas Operacionais', 'Arquitetura de Computadores', 'Redes de Computadores'],
    2: ['Gestão de Pessoas', 'Marketing', 'Finanças Corporativas', 'Empreendedorismo', 'Estatística'],
    3: ['Direito Civil', 'Direito Penal', 'Direito Constitucional', 'Teoria do Estado', 'Direito Administrativo'],
    4: ['Anatomia Humana', 'Fisiologia', 'Farmacologia', 'Patologia', 'Clínica Médica'],
    5: ['Teorias Psicológicas', 'Psicologia do Desenvolvimento', 'Psicopatologia', 'Psicologia Social', 'Neuropsicologia'],
    6: ['Mecânica dos Solos', 'Estruturas de Concreto', 'Topografia', 'Hidráulica', 'Materiais de Construção'],
    7: ['Contabilidade Geral', 'Auditoria', 'Contabilidade de Custos', 'Legislação Tributária', 'Controladoria'],
    8: ['Projeto Arquitetônico', 'Desenho Técnico', 'Conforto Ambiental', 'História da Arquitetura', 'Urbanismo'],
    9: ['Fundamentos da Enfermagem', 'Saúde Coletiva', 'Enfermagem Médico-Cirúrgica', 'Pediatria', 'Ginecologia e Obstetrícia'],
    10: ['Redação Publicitária', 'Mídia e Planejamento', 'Criação Publicitária', 'Comportamento do Consumidor', 'Design Gráfico']
}

# Gera arquivo CSV com id_curso e disciplinas
with open('disciplinas_por_curso.csv', mode='w', newline='', encoding='utf-8') as arquivo_csv:
    escritor = csv.writer(arquivo_csv)
    escritor.writerow(['id_curso', 'nome_curso', 'nome_disciplina'])

    for id_curso, nome_curso in cursos.items():
        disciplinas = disciplinas_por_curso.get(id_curso, [])
        for disciplina in disciplinas:
            escritor.writerow([id_curso, nome_curso, disciplina])

print("Arquivo 'disciplinas_por_curso.csv' gerado com sucesso.")
