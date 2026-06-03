#Importando as bibliotecas
import csv
import sqlite3

# Abrir o arquivo de csv com os dados de produção de alimentos
with open ('producao_alimentos.csv', 'r', encoding = 'utf-8') as file:
    # Criar um leitor de csv
    reader = csv.reader(file)
    
    # Pular a primeira linha do csv que é o cabeçalho
    next(reader)
    
    # Criar uma conexão com o DB
    conn = sqlite3.connect('eng_eba.db')
    
    # Inserir lógica caso a tabela já exista
    conn.execute('DROP TABLE IF EXISTS producao')
    
    # Criar tabela novamente
    conn.execute(''' CREATE TABLE producao (
             produto TEXT,
             quantidade REAL,
             preco_medio REAL,
             receita_total REAL, 
             custo_kg REAL,
             margem_lucro_porcemtagem REAL
             )
    ''')
    
    # Inserir os dados do csv no banco de dados
    for row in reader:
        # Filtra produtos com qtd maiores do que 10
        if float(row[1]) > float(10):
        
            # Calcula a margem de lucro do produto
            margem_lucro = (float(row[3]) - float(row[1]) * float(row[4])) / float(row[3]) * 100
            
            conn.execute('INSERT INTO producao (produto, quantidade, preco_medio, receita_total, custo_kg, margem_lucro_porcemtagem) VALUES (?,?,?,?,?,?)', (row[0], row[1], row[2], row[3], row[4], margem_lucro) )
    
    conn.commit()
    conn.close()
    
print("Pipiline concluído com sucesso.")

# Verificar se os dados estão na base de dados

def verficiar_tabela(banco_dados, tabela):
    conn = sqlite3.connect(banco_dados)

    cursor = conn.cursor()

    cursor.execute(f"SELECT * FROM {tabela}")

    resultados = cursor.fetchall()

    return resultados
    
dados = verficiar_tabela('eng_eba.db', 'producao')
print(dados)

for linha in dados:
    print(linha)