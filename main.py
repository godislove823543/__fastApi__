from fastapi import FastAPI
from datetime import datetime
import sqlite3
from sqlite3 import Error

app = FastAPI()

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def create_table(conn):
    sql_tasks = """
    CREATE TABLE IF NOT EXISTS iot1(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT NOT NULL,
        light REAL NOT NULL,
        temperature REAL NOT NULL
    );
    """

    try:
        cursor = conn.cursor()
        cursor.execute(sql_tasks)
    except:
        print("error")

def insert_project(conn, project):
    sql = """
    INSERT INTO iot1(date,light,temperature)
    VALUES(?,?,?)
    """
    cursor = conn.cursor()
    cursor.execute(sql,project)
    conn.commit()

@app.get("/")
def read_root():
    return {"Hello": "robert"}

@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}

#query parameter
@app.get("/raspberry")
async def read_item(time:str = datetime.now().strftime("%Y%m%d %H:%M:%S"),light: float = 0.0, temperature: float = 0.0):
    conn = create_connection('data.db')
    create_table(conn)
    insert_project(conn, (time,light,temperature))
    conn.close()

    return {
        "時間":time,
        "光線":light,
        "溫度":temperature
    }