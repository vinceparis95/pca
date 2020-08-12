from flask import Flask, render_template, request
from sqlalchemy import create_engine
from flask_mysqldb import MySQL
import pandas as pd
import matplotlib.pyplot as plt

db_connection_str = 'mysql+pymysql://root:Photon959@localhost/pcadata'
db_connection = create_engine(db_connection_str)

df = pd.read_sql_query('SELECT * FROM Circle', con=db_connection)
print("dataframe:\n", df)
print("df shape: ", df.shape, "\n")
print("df description: \n\n", df.describe(), "\n")
df.plot(kind='scatter',x='fname',y='age',color='chartreuse')
plt.tight_layout()
plt.show()
df.to_csv("/Users/vincentparis/dev/pca/mL/circle.csv")
db_connection_str = 'mysql+pymysql://root:Photon959@localhost/pcadata'
db_connection = create_engine(db_connection_str)
