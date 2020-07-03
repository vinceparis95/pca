from flask import Flask, render_template, request
from sqlalchemy import create_engine
from flask_mysqldb import MySQL
import pymysql
import pandas as pd

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Photon959'
app.config['MYSQL_DB'] = 'pcadata'

mysql = MySQL(app)

db_connection_str = 'mysql+pymysql://root:Photon959@localhost/pcadata'
db_connection = create_engine(db_connection_str)

df = pd.read_sql('SELECT * FROM MyUsers', con=db_connection)
print(df)
print("aloha")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        firstName = details['fname']
        lastName = details['lname']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO MyUsers(firstName, lastName) VALUES (%s, %s)", (firstName, lastName))
        mysql.connection.commit()
        cur.close()
    return render_template('index.html', flask_token="Allahuabha : ) ")


if __name__ == '__main__':
    app.debug=True
    app.run()
