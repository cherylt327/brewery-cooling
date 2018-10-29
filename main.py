#!/usr/bin/python
from flask import Flask, request, redirect, render_template, session, flash
import pymysql.cursors
from datetime import date 

app = Flask(__name__)
connection = pymysql.connect(
    host="localhost", 
    user="brew",
    password="Bauser76!",
    db="brewery",
    charset='utf8',
    cursorclass=pymysql.cursors.DictCursor

)


with connection.cursor() as cursor:
    recipe_sql="select id,name from recipes"; 
    cursor.execute(recipe_sql)
    recipes = cursor.fetchall()

    ferm_sql="select pos as pos from ferm_pos where temp_serial is not null order by pos"; 
    cursor.execute(ferm_sql)
    fermenters=cursor.fetchall()

@app.route('/', methods  = ['POST','GET'])
def main_display():
    message = ""
    if request.method == 'POST':
        recipe_id = str(request.form['recipe'])
        pos = str(request.form['pos'])
        
        if recipe_id == "" or pos == "": 
            message = "You did not fill out a required field"
        else:
            today = str(date.today())
            try:
                with connection.cursor() as cursor:
                    sql_enter_brew = "insert into ferm(pos,recipe_id,start_date) values(%s,%s,%s)"
                    val = (pos,recipe_id,today)
                    cursor.execute(sql_enter_brew,val)
                    connection.commit()
                    message="Brewing has commenced!!!"
                    connection.close
            except connection.error as err:
                message = err
            
           
    return render_template('index.html',title='Brew Beer',recipes=recipes,fermenters=fermenters,message=message)
    
if __name__ == '__main__':
    app.debug = True
    app.run()

