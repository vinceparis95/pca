from flask import (Flask, request, render_template)
from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask("__main__")

mysql = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://"+os.environ['Administrator'] + ":" + os.environ['Photon959']+ "@" + os.environ['pcadata.cfylo90nqrvk.us-east-2.rds.amazonaws.com'] +":3306/innodb"


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        firstName = details['fname']
        lastName = details['lname']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO MyUsers(firstName, lastName) VALUES (%s, %s)", (firstName, lastName))
        db.connection.commit()
        cur.close()
        return 'success'
    return render_template('index.html')

app.run(debug=True)
