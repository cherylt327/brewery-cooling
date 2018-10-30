#!/usr/bin/python
import pymysql.cursors
import time
import os
import glob
from datetime import datetime
from datetime import date
from pathlib import Path 
from RPi import GPIO

    # Read the raw device data from temp probe # 
def red_temp_raw(serial):
    base_dir = '/sys/bus/w1/devices/'
    device_file = glob.glob(base_dir + serial)[0] + 'w1_slave' 
    f = open(device_file,'r')
    lines = f.readlines()
    f.close()
    return lines

    # Convert the raw device data into human readable #
def read_temp(serial):
    lines = read_temp_raw(serial)
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw(serial)
        equals_pos = lines[1].find('t=')
        if equals_pos != -1: 
            temp = int(lines[1][equals_pos+2])
            temp_f = str(round((temp / 1000.0) * 9.0 / 5.0 + 32.0))
            temp_c = str(round((temp / 1000.0)))
            temperatures = {"F":temp_f,"C":temp_c} 
    return temperatures

def date_diff(d1, d2): 
    d1 = datetime.strptime(d1,"%Y-%m-%d")
    d2 = datetime.strptime(d2,"%Y-%m-%d")
    return abs((d2-d1).days)

today = str(date.today())

connection = pymysql.connect(
        host="localhost",
        user="brew",
        password="Bauser76!", 
        db="brewery",
        charset="utf8", 
        cursorclass=pymysql.cursors.DictCursor
        )

with connection.cursor() as cursor: 

        # Get currently fermenting beer #

    sql_fermenting = "select pos,recipe_id,start_date from ferm"
    cursor.execute(sql_fermenting)
    fermenting = cursor.fetchall()

for ferment in fermenting:

        # Get fermentation intervals 64 degrees for 5 dayas etc #

    sql_intervals = "select start_temp,end_temp,days from recipe_intervals where recipe_id =%s"
    val = (ferment['recipe_id'])
    cursor.execute(sql_intervals,val)
    intervals = cursor.fetchall()

        # Get the fermenter pos information inc rpi gpio output and temperatur probe serial #

    sql_pos = "select gpio,temp_serial from ferm_pos where pos = %s"
    val = (ferment['pos'])
    cursor.execute(sql_pos,val)
    positions = cursor.fetchall()


    days = 0 
    old_days = 0
    gpio = positions[0]['gpio']
    gpio_lock_file = '/opt/fermenters/gpio_'+gpio+'.lock'
    temp_serial = positions[0]['temp_serial'] 
    temperatures = read_temp(temp_serial)
    c = 0

        # Loop through fermenting intervals # 

    for interval in intervals: 
        days += interval['days']
        start = str(interval['start_date'])
        end = today
        day_diff = date_diff(start,end)

            # if today is before the end of the current interval # 
            # and today is after the end of the previous interval #

        if day_diff <= days and day_diff >= old_days: 
            if int(temperatures['F']) > int(interval['end_temp']):
                    # OPEN VALVE
                if not Path(gpio_lock_file).is_file():
                    # CREATE LOCK FILE #
            elif int(temperatures['F']) < int(interval['end_temp']):
                # CLOSE VALVE # 
                if Path(gpio_lock_file).is_file(): 
                        # REMOVE LOCK FILE # 
        c += 1        
        old_days = days

            # If we're on the last brewing interval and today is after the last day #

        if c == len(intervals) and day_diff > old_days and Path(gpio_lock_file).is_file(): 
            # CLOSE VALVE # 
            # REMOVE LOCK FILE # 
