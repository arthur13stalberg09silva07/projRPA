from os import getenv
import psycopg2
from dotenv import load_dotenv

load_dotenv()

class Banco:
    def __init__(self):
        conn = psycopg2.connect(host=getenv("DB_HOST"),
                            database=getenv("DB_DBNAME"),
                            user=getenv("DB_USERNAME"),
                            password=getenv("DB_PASSWORD"),
                            port=getenv("DB_PORT"))
        self.__cur = conn.cursor()
    
    def get_all_carros(self):
        self.__cur.execute("SELECT * FROM carros;")
        carros = []
        carrosFetch = self.__cur.fetchall()

        for row in carrosFetch:
            carros.append({"modelo": row[0], "ano_lancamento": row[1], "cor": row[2], "empresa": row[3]})
        return carros