# 📊 Geração de Dados Fake para Projeto Educacional

Este repositório contém notebooks em Python desenvolvidos para gerar dados sintéticos (fakes) utilizados em um projeto educacional. O objetivo é facilitar testes, análises e validações de pipelines ou sistemas que utilizam dados de contexto acadêmico, sem comprometer a privacidade de dados reais.

## 📁 Estrutura dos Dados Gerados

Os notebooks geram os seguintes conjuntos de dados simulados:

### 🧑‍🎓 Alunos

Contém informações básicas dos estudantes matriculados.

| Campo        | Descrição                    |
| ------------ | ---------------------------- |
| `matricula`  | Identificador único do aluno |
| `nome_aluno` | Nome completo do aluno       |
| `id_curso`   | Identificador do curso       |

---

### 🧾 Alunos Matriculados

Representa os dados mais completos dos alunos com informações adicionais.

| Campo             | Descrição                              |
| ----------------- | -------------------------------------- |
| `matricula`       | Identificador único do aluno           |
| `nome_aluno`      | Nome completo do aluno                 |
| `id_curso`        | Identificador do curso                 |
| `data_nascimento` | Data de nascimento do aluno            |
| `endereco`        | Endereço fictício do aluno             |
| `status`          | Situação do aluno (ativo, inativo etc) |

---

### 🎓 Cursos

Contém os cursos disponíveis no sistema.

| Campo        | Descrição                     |
| ------------ | ----------------------------- |
| `id_curso`   | Identificador único do curso  |
| `nome_curso` | Nome do curso                 |
| `nota_curso` | Nota média atribuída ao curso |

---

### 📚 Disciplinas

Lista as disciplinas vinculadas a cada curso.

| Campo             | Descrição                                |
| ----------------- | ---------------------------------------- |
| `id_disciplina`   | Identificador único da disciplina        |
| `id_curso`        | Curso ao qual a disciplina pertence      |
| `nome_curso`      | Nome do curso (redundância para análise) |
| `nome_disciplina` | Nome da disciplina                       |

---

### 🕒 Acessos

Representa os acessos realizados pelos alunos a uma plataforma de ensino.

| Campo               | Descrição                    |
| ------------------- | ---------------------------- |
| `matricula`         | Identificador do aluno       |
| `timestamp_acesso`  | Data e hora do acesso        |
| `tempo_duracao_min` | Duração do acesso em minutos |

---

## 🚀 Objetivo

Este conjunto de dados simula uma estrutura educacional típica e pode ser utilizado para:

* Desenvolvimento e teste de pipelines de dados
* Análise exploratória (EDA)
* Treinamento de modelos de machine learning
* Simulação de dashboards educacionais

## 🛠️ Tecnologias Utilizadas

* Python
* Faker

## 📌 Observações

* Os dados gerados são totalmente fictícios.
* É possível personalizar a quantidade e complexidade dos dados via parâmetros nos notebooks.
