# Projeto E-commerce

> **Projeto em desenvolvimento**

Projeto desenvolvido durante meus estudos de **Análise de Dados com Python e Pandas**, com o objetivo de praticar a criação, manipulação e análise de dados de um cenário de vendas.

## Tecnologias

- Python
- Pandas
- SQL
- SQLite
- Streamlit

## Conceitos praticados

- Criação e manipulação de DataFrames;
- Geração e organização de dados;
- Leitura de arquivos CSV;
- Exportação de dados para CSV e Excel;
- Seleção de colunas;
- Filtragem de dados;
- `merge`;
- `rename`;
- `reset_index`;
- `set_index`;
- `value_counts`;
- Manipulação de datas;
- Funções de agregação;
- `pivot_table`;
- Integração com SQLite;
- Consultas SQL;
- Criação de interfaces com Streamlit.

## Estrutura

- `gera_dataset.py` — geração dos dados do projeto
- `1-visualizando_tb.py` — visualização dos dados com Streamlit
- 2-selecionando_colunas.py	- permite selecionar e filtrar dados
- 3-adicionando_linhas.py	- permite adicionar novas compras
- 4-volume_dados.py	- realiza análises do volume de compras
- 5-tb_dinamica.py - cria análises utilizando tabela dinâmica
- `ecommerce.db` — banco de dados SQLite
- `datasets/` — arquivos CSV e Excel utilizados no projeto

## Como executar localmente

### 1. Clone o repositório
No terminal, execute:
```bash
git clone https://github.com/JulianaRochaDL/projetos-curso-analise-de-dados-python-pandas.git
```

### 2. Acesse a pasta do projeto
Após clonar o repositório, entre na pasta do projeto:
```bash
cd projetos-curso-analise-de-dados-python-pandas
```
```bash
cd projetos-pandas/ecommerce
```

### 3. Instale as dependências
No terminal do VS Code, execute:
```bash
pip install pandas streamlit openpyxl names
```

### 4. Gere os datasets

Execute o arquivo responsável pela geração dos dados:
```bash
python gera_dataset.py
```

### 5. Execute as aplicações
Execute cada aplicação individualmente pelo terminal:
```bash
streamlit run 1-visualizando_tb.py
```
```bash
streamlit run 2-selecionando_colunas.py
```
```bash
streamlit run 3-adicionando_linhas.py
```
```bash
streamlit run 4-volume_dados.py
```
```bash
streamlit run 5-tb_dinamica.py
```

## 6. Aplicação

O projeto utiliza **Streamlit** para criar interfaces interativas de visualização e análise dos dados. Abaixo, é apresentada uma das aplicações desenvolvidas: a tabela dinâmica.

<img width="1193" height="353" alt="image" src="https://github.com/user-attachments/assets/7bfade81-8770-4aaa-82f0-1148779f79fa" />



