#!/usr/bin/python
import json 
import time 
import os 
import glob 
def read_temp_raw(serial):
    base_dir = '/sys/bus/w1/devices/'
    device_file = glob.glob(base_dir + serial)[0] + '/w1_slave'
    f = open(device_file,'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp(serial):
    lines = read_temp_raw(serial)
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw(serial)
    equals_pos = lines[1].find('t=')
    if equals_pos != -1: 
        temp = int(lines[1][equals_pos+2:])
        temp_f = str(round((temp / 1000.0) * 9.0 / 5.0 + 32.0))
        temp_c = str(round((temp / 1000.0)))
        temperatures = {"F":temp_f,"C":temp_c}
        return temperatures





with open('../ferm_pos.json') as data:
    fermenters = json.load(data)
    for fermenter in fermenters:
        if 'temp_serial' in fermenter.keys():
            temperatures = read_temp(fermenter['temp_serial'])
            print(temperatures)
    
