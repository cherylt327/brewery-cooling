#!/usr/bin/python
import json

fermenters={
    1:{"pos":1,"gpio":6,"temp_serial":"28-0417711245ff"}, 
    2:{"pos":2,"gpio":5},
    3:{"pos":3,"gpio":10}, 
    4:{"pos":4,"gpio":22}, 
    5:{"pos":5,"gpio":27}, 
    6:{"pos":6,"gpio":17}, 
    7:{"pos":7,"gpio":9}, 
    8:{"pos":8,"gpio":11}
    }


for fermenter_pos in fermenters:
    print(fermenter_pos)

with open('../ferm_pos.json','w') as outfile:
    json.dump(fermenters, outfile)
