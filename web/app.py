from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL


app= Flask(__name__,template_folder='template')
mysql = MySQL(app)

app.secret_key = 'many random bytes'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root@123'
app.config['MYSQL_DB'] = 'recipeapp'






@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT  * FROM food_items")
    data = cur.fetchall()
    cur.close()

    return render_template('recipe.html',food=data)


@app.route('/insert', methods = ['POST'])
def insert():

    if request.method == "POST":
        flash("Data Inserted Successfully")
        name = request.form['name']
        time = request.form['time']
        diff = request.form['difficulty']
        veg = request.form['vegetarian']
        rate = request.form['rate']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO food_items (food_name,prep_time ,difficulty, vegetarian,rating) VALUES (%s, %s, %s,%s,%s)", (name, time, diff,veg,rate))
        mysql.connection.commit()
        return redirect(url_for('Index'))
    else:
        return render_template('recipe.html')



@app.route('/update',methods=['POST','GET'])
def update():

    if request.method == 'POST':
        id_data = request.form['id']
        name = request.form['name']
        time = request.form['time']
        diff = request.form['difficulty']
        veg = request.form['vegetarian']
        rate = request.form['rate']
        cur = mysql.connection.cursor()
        cur.execute("""
               UPDATE food_items
               SET food_name=%s,prep_time=%s ,difficulty=%s, vegetarian=%s,rating=%s
               WHERE id=%s
            """, (name, time, diff, veg,rate,id_data))
        flash("Data Updated Successfully")
        mysql.connection.commit()
        return redirect(url_for('Index'))


@app.route('/delete/<string:id_data>', methods = ['GET'])
def delete(id_data):
    flash("Record Has Been Deleted Successfully")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM food_items WHERE id=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('Index'))


if __name__ == "__main__":
    app.run(debug=True)