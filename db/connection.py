import psycopg2

def criar_banco_se_nao_existir():
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password="admin",
            port="5432"
        )
        conn.autocommit = True
        cur = conn.cursor()

        cur.execute("SELECT 1 FROM pg_database WHERE datname = 'sistema_turismo_alagoas';")
        existe = cur.fetchone()

        if not existe:
            cur.execute("CREATE DATABASE sistema_turismo_alagoas;")
            print("Banco de dados 'sistema_turismo_alagoas' criado com sucesso!")
        else:
            print("ℹBanco de dados já existe.")

        cur.close()
        conn.close()

    except psycopg2.Error as e:
        print("Erro ao verificar/criar o banco:", e)


def get_connection():
    try:
        connection = psycopg2.connect(
            host="localhost",
            database="sistema_turismo_alagoas",
            user="postgres",
            password="admin",
            port="5432"
        )
        return connection
    except psycopg2.Error as e:
        print("Erro ao conectar ao banco de dados:", e)
        return None


def testar_conexao():
    criar_banco_se_nao_existir()
    conn = get_connection()
    if conn:
        print("Conexão com o banco de dados bem-sucedida!")
        conn.close()
    else:
        print("Falha na conexão com o banco de dados.")


if __name__ == "__main__":
    testar_conexao()