#!/usr/bin/python
import json
import sys
from datetime import datetime
from datetime import date
def date_diff(d1, d2): 
    d1 = datetime.strptime(d1,"%Y-%m-%d")
    d2 = datetime.strptime(d2,"%Y-%m-%d")
    return abs((d2-d1).days)

today = str(date.today())

with open ('fermenting.json') as data:
    current_ferm = json.load(data)
with open('ferm_pos.json') as data: 
    ferm_pos = json.load(data)
with open('recipes.json') as data:
    recipes = json.load(data)

for ferm in current_ferm:
    recipe_pos = int(ferm['ferm_pos'])
    recipe_no = int(ferm['recipe_no'])
   # Loop through ferm_pos instead of current_ferm???? #
    recipe = recipes[str(recipe_no)]
    days = 0 
    old_days = 0
    gpio = ferm_pos[str(recipe_pos)]['gpio']
    gpio_lock_file = 'gpio_'+str(gpio)+'.lock'
    serial = ferm_pos[str(recipe_pos)]['temp_serial']
    print(serial)
    print(recipe)
    for segment in recipe['segments']:
        days += int(segment['days'])
        start = ferm['start_date']
        diff = date_diff(start,today)
        print(diff)




