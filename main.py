#!/usr/bin/python
from flask import Flask, request, redirect, render_template, session, flash
import mysql.connector

app = Flask(__name__)
mydb = mysql.connector.connect(
    host="localhost", 
    user="brew",
    password="Bauser76!",
    database="brewery"
)
mycursor = mydb.cursor(dictionary=True)

recipe_sql="select id,name from recipes"; 
mycursor.execute(recipe_sql)
recipes = mycursor.fetchall()

ferm_sql="select pos as pos from ferm_pos where temp_serial is not null order by pos"; 
mycursor.execute(ferm_sql)
fermenters=mycursor.fetchall()

print(recipes)
print(fermenters)
@app.route('/', methods  = ['POST'])
def main_display():
    return render_template('index.html',title='Brew Beer',recipes=recipes,fermenters=fermenters)
