import requests
import mysql.connector
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os

# Carrega as variáveis do arquivo .env
load_dotenv()

# Conectar ao banco de dados MySQL
def get_db_connection():
    return mysql.connector.connect(
        host = os.getenv('DB_HOST'),
        user = os.getenv('DB_USER'),
        password = os.getenv('DB_PASS'),
        database = os.getenv('DB_NAME')
    )

# Salvar o token no banco de dados
def save_token_to_db(id, access_token, refresh_token, expires_in, updated_at):
    expires_at = datetime.now() + timedelta(seconds=expires_in)
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Verificar se já existe um token no banco de dados
    cursor.execute(f"SELECT id FROM tokens WHERE id = {id}")
    result = cursor.fetchone()
    print(result)
    if result:
        # print(f"Item: {result}")
        # Atualizar o token existente
        query = """
          UPDATE tokens SET access_token = %s, refresh_token = %s, expires_in = %s, expires_at = %s, updated_at = %s WHERE id = %s
        """
        cursor.execute(query, (access_token, refresh_token, expires_in, expires_at, updated_at, id))
    else:
        # Inserir um novo token
        query = """
          INSERT INTO tokens (access_token, refresh_token, expires_in, expires_at) VALUES (%s, %s, %s, %s)
        """
        cursor.execute(query, (access_token, refresh_token, expires_in, expires_at))
    
    conn.commit()
    cursor.close()
    conn.close()

# Obter o token do banco de dados
def get_token_from_db():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM save_token_tagplus.tokens")
    tokens = cursor.fetchall()
    cursor.close()
    conn.close()
    return tokens

# Função para fazer o refresh do token
def refresh_token():
    url = "https://api.tagplus.com.br/oauth2/token"
    datas = get_token_from_db()

    for data in datas:
        client_id = data['client_id']
        client_secret = data['client_secret']
        refresh_token = data['refresh_token']
        updated_at = datetime.now()

        if data:
            # Verificar se o token ainda é válido
            if datetime.now() < data['expires_at']:
                print(f"O token da {data['company']} ainda é válido.")
                continue
        
        if not data or 'refresh_token' not in data:
            raise Exception("Nenhum token encontrado no banco de dados ou refresh_token está ausente.")
        
        payload = {
            'grant_type': 'refresh_token',
            'refresh_token': refresh_token,
            'client_id': client_id,
            'client_secret': client_secret
        }
    
        response = requests.post(url, data=payload)

        print(f"Buscando token da {data['company']} ...")
        if response.status_code == 200:
            token_info = response.json()
            
            if 'access_token' in token_info:
                save_token_to_db(data['id'], token_info['access_token'], token_info['refresh_token'], token_info['expires_in'], updated_at)
                print(f"Informações de acesso da {data['company']} foram atualizadas!")
                print(token_info)
            else:
                raise Exception("Falha ao obter novo token: {}".format(token_info))
        else:
            raise Exception(f"Erro ao fazer o refresh do token. Status Code: {response.status_code}")

#Chamando refresh_token
try:
    refresh_token()
except Exception as e:
    print(e)