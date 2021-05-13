from flask import Flask, Markup, render_template

app = Flask(__name__)

import numpy as np
import matplotlib.pyplot as plt
import os
import mysql.connector
import json
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="csv_db 7"
)
mycursor = mydb.cursor()
sql="select count(*) from `google_play_apps_data_sample_1` WHERE `Rating_value` > 4.0 AND `Rating_value` <= 5.0"
mycursor.execute(sql)
Rating_apps = mycursor.fetchone()
Rating_5_json = json.dumps(Rating_apps)
Rating_5_json = Rating_5_json.replace("[", "")
Rating_5_json = Rating_5_json.replace("]", "")
Rating_5_json=int(Rating_5_json)
print(Rating_5_json)

sql="select count(*) from `google_play_apps_data_sample_1` WHERE `Rating_value` > 3.0 AND `Rating_value` <= 4.0"
mycursor.execute(sql)
Rating_apps = mycursor.fetchone()
Rating_4_json = json.dumps(Rating_apps)
Rating_4_json = Rating_4_json.replace("[", "")
Rating_4_json = Rating_4_json.replace("]", "")
Rating_4_json=int(Rating_4_json)
print(Rating_4_json)

sql="select count(*) from `google_play_apps_data_sample_1` WHERE `Rating_value` > 2.0 AND `Rating_value` <= 3.0"
mycursor.execute(sql)
Rating_apps = mycursor.fetchone()
Rating_3_json = json.dumps(Rating_apps)
Rating_3_json = Rating_3_json.replace("[", "")
Rating_3_json = Rating_3_json.replace("]", "")
Rating_3_json=int(Rating_3_json)
print(Rating_3_json)

sql="select count(*) from `google_play_apps_data_sample_1` WHERE `Rating_value` > 1.0 AND `Rating_value` <= 2.0"
mycursor.execute(sql)
Rating_apps = mycursor.fetchone()
Rating_2_json = json.dumps(Rating_apps)
Rating_2_json = Rating_2_json.replace("[", "")
Rating_2_json = Rating_2_json.replace("]", "")
Rating_2_json=int(Rating_2_json)
print(Rating_2_json)

sql="select count(*) from `google_play_apps_data_sample_1` WHERE `Rating_value` <= 1.0"
mycursor.execute(sql)
Rating_apps = mycursor.fetchone()
Rating_1_json = json.dumps(Rating_apps)
Rating_1_json = Rating_1_json.replace("[", "")
Rating_1_json = Rating_1_json.replace("]", "")
Rating_1_json=int(Rating_1_json)
print(Rating_1_json)
# creating the dataset
data = {'<=1.0':Rating_1_json, '1.0 - 2.0':Rating_2_json, '2.0 - 3.0':Rating_3_json,
        '3.0 - 4.0':Rating_4_json,'4.0 - 5.0': Rating_5_json}
courses = list(data.keys())
values = list(data.values())
  
fig = plt.figure(figsize = (10, 5))
 
# creating the bar plot
plt.bar(courses, values, color ='ORANGE',
        width = 0.4)
 
plt.xlabel("ĐIỂM ĐÁNH GIÁ")
plt.ylabel("SỐ LƯỢNG ỨNG DỤNG")
file_name = 'RATING_APPS_1.png'
# change the current working
# directory
os.chdir("E:/NT114/app/static/")
my_path = os.path.abspath(file_name)
plt.savefig(my_path, transparent=True)