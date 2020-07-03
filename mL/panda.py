from flask import Flask, render_template, request
from sqlalchemy import create_engine
from flask_mysqldb import MySQL
import pandas as pd

db_connection_str = 'mysql+pymysql://root:Photon959@localhost/pcadata'
db_connection = create_engine(db_connection_str)

df = pd.read_sql_query('SELECT * FROM MyUsers', con=db_connection)
print(df)
df.to_csv("/Users/vincentparis/dev/pca/mL/out.csv")
db_connection_str = 'mysql+pymysql://root:Photon959@localhost/pcadata'
db_connection = create_engine(db_connection_str)

df = pd.read_sql('SELECT * FROM MyUsers', con=db_connection)
print(df)
