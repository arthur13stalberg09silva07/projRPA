from os import getenv
import psycopg2
from dotenv import load_dotenv

load_dotenv()

def get_db_connection():
    conn = psycopg2.connect(host=getenv("DB_HOST"),
                            database=getenv("DB_DBNAME"),
                            user=getenv("DB_USERNAME"),
                            password=getenv("DB_PASSWORD"),
                            port=getenv("DB_PORT"))
    return conn

def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM registers;')
    
    cur.close() 
    conn.close()