
from flask import Flask
from flask_mysqldb import MySQL

app= Flask(__name__)
mysql=MySQL()
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']='root@123'
app.config['MYSQL_DB']='recipeapp'

mysql.init_app(app)