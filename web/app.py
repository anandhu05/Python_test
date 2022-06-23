from flask import Flask, render_template
from flask_mysqldb import MYSQL
import yaml

app= Flask(__name__,template_folder='template')

db=yaml.load(open('db.yaml'))
app.config['MYSQL_HOST']=db['mysql_host']
app.config['MYSQL_USER']=db['mysql_user']
app.config['MYSQL_PASSWORD']=db['mysql_password']
app.config['MYSQL_DB']=db['mysql_db']

mysql=MYSQL(app)
@app.route('/',methods=['GET','POST'])
def home():
    return render_template('recipe.html')

if __name__ == '__main__':
    app.run(debug=True)
