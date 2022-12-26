from aplication import app
from flask_mysqldb import MySQL
from MySQLdb.cursors import Cursor

app.config["MYSQL_HOST"] = '127.0.0.1'
app.config["MYSQL_USER"] = 'root'
app.config["MYSQL_PASSWORD"] = 'admin'
app.config["MYSQL_DB"] = 'task_api'
app.config["MYSQL_PORT"] = '3306'

mysql = MySQL(app)

def execute(sql: str) -> Cursor:
    cursor = mysql.connection.cursor()
    cursor.execute(sql)
    return cursor

def commit() -> None:
    mysql.connection.commit()