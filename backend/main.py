from flask import (Flask, request, render_template)
from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config["DEBUG"] = True
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:Photon959@localhost/pcadata"
app.config["SQLALCHEMY_ECHO"] = True
db = SQLAlchemy(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        firstName = details['fname']
        lastName = details['lname']
        cur = db.connection.cursor()
        cur.execute("INSERT INTO MyUsers(firstName, lastName) VALUES (%s, %s)", (firstName, lastName))
        db.connection.commit()
        cur.close()
        return 'success'
    return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    app.run()
