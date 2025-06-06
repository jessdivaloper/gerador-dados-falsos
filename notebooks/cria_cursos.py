import pandas as pd

# Criar a tabela com dados fictícios
data = {
    "curso_id": range(1, 11),
    "nome_curso": [
        "Engenharia de Computação", "Administração", "Direito",
        "Medicina", "Psicologia", "Engenharia Civil",
        "Ciências Contábeis", "Arquitetura e Urbanismo", 
        "Enfermagem", "Publicidade e Propaganda"
    ],
    "nota_curso": [4.5, 3.8, 4.2, 4.9, 4.0, 4.1, 3.7, 4.3, 4.0, 3.9]
}

df_cursos = pd.DataFrame(data)

# Salvar em CSV
csv_path = "/cursos_universitarios.csv"
df_cursos.to_csv(csv_path, index=False)

csv_path
