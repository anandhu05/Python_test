from flask import Flask, render_template
from flask_mysqldb import MySQL
import getdata
import mysql.connector
app= Flask(__name__,template_folder='template')
connection=mysql.connector.connect(host='localhost',database='recipeapp',user="root",password="root@123")
cursor1=connection.cursor()
#mysql=MySQL(app)
@app.route('/',methods=['GET','POST'])
def home():
    return render_template('recipe.html')

if __name__ == '__main__':
    app.run(debug=True)


def getData():
    objGetData = getdata.getDatas()
    aData=objGetData.getAlldata()