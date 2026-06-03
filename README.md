# 📊 Pipeline de Engenharia de Dados: Análise de Produção de Alimentos

[cite_start]Este projeto consiste no desenvolvimento de uma pipeline ETL (Extração, Limpeza, Transformação e Carga) para processar dados diários de produção de alimentos[cite: 4, 8]. [cite_start]O objetivo principal é automatizar o tratamento de dados brutos armazenados em arquivos CSV, aplicar regras de negócio para calcular indicadores de rentabilidade e centralizar as informações consolidadas em um banco de dados SQLite para consultas futuras[cite: 5, 6, 9].

---

## 🏢 Cenário de Negócio

[cite_start]Em uma empresa do setor alimentício, a equipe de produção coleta registros diários contendo a quantidade produzida, preço médio de venda e receita gerada por item[cite: 3, 4]. [cite_start]No entanto, esses dados brutos chegam com certas inconsistências de formatação (como pontos atuando como separadores de milhar nos valores financeiros) e precisam passar por um processo de limpeza, transformação e enriquecimento antes de serem utilizados para análise e tomada de decisão[cite: 5, 14, 15].

[cite_start]O desafio central foi criar um fluxo automatizado que execute o tratamento dessas informações, calcule a margem de lucro real de cada produto e disponibilize os dados estruturados para a equipe de análise de negócios[cite: 6, 8, 20].

---

## 🛠️ Arquitetura e Etapas da Pipeline (ETL)

[cite_start]A pipeline foi construída seguindo as etapas clássicas de engenharia de dados[cite: 8]:

1. [cite_start]**Extração:** Os dados de produção de alimentos são extraídos de um arquivo CSV de origem, onde cada linha contém informações sobre um produto, quantidade, preço médio e receita total[cite: 12, 13].
2. [cite_start]**Limpeza:** Remoção de pontos que servem como separadores de milhar nos valores financeiros, permitindo que os dados sejam manipulados numericamente de forma correta[cite: 14, 15].
3. [cite_start]**Transformação & Filtragem:** * **Regra de Filtro:** Apenas produtos com uma quantidade superior a 10 unidades são considerados para a análise[cite: 6, 18].
   * [cite_start]**Métrica de Negócio:** Cálculo da margem de lucro percentual de cada produto através da fórmula[cite: 16]:
     
     $$margem\_lucro\_porcentagem = \frac{(Receita~Total) - (Quantidade \times Custo~por~kg)}{Receita~Total} \times 100$$
     
4. **Enriquecimento & Armazenamento:** A nova coluna com a margem de lucro calculada é integrada aos dados e o conjunto final enriquecido é inserido em uma tabela de um banco de dados SQLite (`eng_eba.db`)[cite: 9, 19, 20].

---

## 📂 Estrutura do Projeto

Com base na organização do diretório, a estrutura de arquivos do projeto se apresenta da seguinte forma:

```text
├── .venv/                   # Ambiente virtual do Python (gerenciado pelo Poetry)
├── .gitignore               # Arquivos e pastas ignorados pelo Git
├── .python-version          # Versão do interpretador Python do projeto
├── eng_eba.db               # Banco de dados SQLite gerado pela pipeline
├── pipiline.py              # Script principal com o código da pipeline ETL
├── poetry.lock              # Travamento de versões das dependências do Poetry
├── producao_alimentos.csv   # Arquivo fonte contendo os dados brutos de produção
├── pyproject.toml           # Configurações do projeto e dependências do ambiente
└── testes.ipynb             # Jupyter Notebook para prototipagem e testes analíticos