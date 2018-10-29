#!/usr/bin/python
import json
from datetime import date
import sys
today = str(date.today())
screen =""
with open ('recipes.json') as data:
    recipes = json.load(data)
    for recipe_no in recipes:
      screen = screen + recipes[recipe_no]['name'] + ' - ' + recipe_no + '\r\n'
    screen = screen + 'Select Recipe #'
sel_recipe = input(screen)
ferm_pos = input('Enter Fermenter #: 1-4')

message = ""
with open ('fermenting.json') as data: 
    current_ferm = json.load(data)
    for item in current_ferm: 
        if item['ferm_pos'] == ferm_pos: 
            message = "There\'s already beer there."

if message != "": 
    print(message)
else: 
    fermenting = {"start_date":today,"recipe_no":sel_recipe,"ferm_pos":ferm_pos}
    with open('fermenting.json') as data:
        data = json.load(data)
        data.append(fermenting)
        with open('fermenting.json','w') as write:
            json.dump(data, write)

