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
#Lấy dữ liệu tổng số ứng dụng và năm cách đây 11 năm
sql_6_1="SELECT COUNT(*) as app_number FROM `google_play_apps_data_sample_1` WHERE year(`Date_launch`) <= YEAR(CURDATE() - INTERVAL 11 YEAR)"
mycursor.execute(sql_6_1)
All_apps_6_json = mycursor.fetchone()
All_apps_6 = json.dumps(All_apps_6_json)
All_apps_6 = All_apps_6.replace("[", "")
All_apps_6 = All_apps_6.replace("]", "")
All_apps_6=int(All_apps_6)
print(All_apps_6)
sql_6_2="SELECT year(`Date_launch`) as year FROM `google_play_apps_data_sample_1` WHERE year(`Date_launch`) = YEAR(CURDATE() - INTERVAL 11 YEAR) LIMIT 0,1"
mycursor.execute(sql_6_2)
years_6_json = mycursor.fetchone()
years_6 = json.dumps(years_6_json)
years_6 = years_6.replace("[", "")
years_6 = years_6.replace("]", "")
years_6=int(years_6)
print(years_6)

#Lấy dữ liệu tổng số ứng dụng và năm cách đây 10 năm
sql_5_1="SELECT COUNT(*) as app_number FROM `google_play_apps_data_sample_1` WHERE year(`Date_launch`) <= YEAR(CURDATE() - INTERVAL 10 YEAR)"
mycursor.execute(sql_5_1)
All_apps_5_json = mycursor.fetchone()
All_apps_5 = json.dumps(All_apps_5_json)
All_apps_5 = All_apps_5.replace("[", "")
All_apps_5 = All_apps_5.replace("]", "")
All_apps_5=int(All_apps_5)
print(All_apps_5)
sql5_2="SELECT year(`Date_launch`) as year FROM `google_play_apps_data_sample_1` WHERE year(`Date_launch`) = YEAR(CURDATE() - INTERVAL 10 YEAR) LIMIT 0,1"
mycursor.execute(sql5_2)
years_5_json = mycursor.fetchone()
years_5 = json.dumps(years_5_json)
years_5 = years_5.replace("[", "")
years_5 = years_5.replace("]", "")
years_5 = int(years_5)
print(years_5)

#Lấy dữ liệu tổng số ứng dụng và năm cách đây 9 năm
sql="SELECT COUNT(*) as app_number FROM `google_play_apps_data_sample_1` WHERE year(`Date_launch`) <= YEAR(CURDATE() - INTERVAL 9 YEAR)"
mycursor.execute(sql)
All_apps_4_json = mycursor.fetchone()
All_apps_4 = json.dumps(All_apps_4_json)
All_apps_4 = All_apps_4.replace("[", "")
All_apps_4 = All_apps_4.replace("]", "")
All_apps_4 = int(All_apps_4)
print(All_apps_4)
sql="SELECT year(`Date_launch`) as year FROM `google_play_apps_data_sample_1` WHERE year(`Date_launch`) = YEAR(CURDATE() - INTERVAL 9 YEAR) LIMIT 0,1"
mycursor.execute(sql)
years_4_json = mycursor.fetchone()
years_4 = json.dumps(years_4_json)
years_4 = years_4.replace("[", "")
years_4 = years_4.replace("]", "")
years_4 = int(years_4)
print(years_4)

#Lấy dữ liệu tổng số ứng dụng và năm cách đây 8 năm
sql="SELECT COUNT(*) as app_number FROM `google_play_apps_data_sample_1` WHERE year(`Date_launch`) <= YEAR(CURDATE() - INTERVAL 8 YEAR)"
mycursor.execute(sql)
All_apps_3_json = mycursor.fetchone()
All_apps_3 = json.dumps(All_apps_3_json)
All_apps_3 = All_apps_3.replace("[", "")
All_apps_3 = All_apps_3.replace("]", "")
All_apps_3 = int(All_apps_3)
print(All_apps_3)
sql="SELECT year(`Date_launch`) as year FROM `google_play_apps_data_sample_1` WHERE year(`Date_launch`) = YEAR(CURDATE() - INTERVAL 8 YEAR) LIMIT 0,1"
mycursor.execute(sql)
years_3_json = mycursor.fetchone()
years_3 = json.dumps(years_3_json)
years_3 = years_3.replace("[", "")
years_3 = years_3.replace("]", "")
years_3 = int(years_3)
print(years_3)

#Lấy dữ liệu tổng số ứng dụng và năm cách đây 7 năm
sql="SELECT COUNT(*) as app_number FROM `google_play_apps_data_sample_1` WHERE year(`Date_launch`) <= YEAR(CURDATE() - INTERVAL 7 YEAR)"
mycursor.execute(sql)
All_apps_2_json = mycursor.fetchone()
All_apps_2 = json.dumps(All_apps_2_json)
All_apps_2 = All_apps_2.replace("[", "")
All_apps_2 = All_apps_2.replace("]", "")
All_apps_2 = int(All_apps_2)
print(All_apps_2)
sql="SELECT year(`Date_launch`) as year FROM `google_play_apps_data_sample_1` WHERE year(`Date_launch`) = YEAR(CURDATE() - INTERVAL 7 YEAR) LIMIT 0,1"
mycursor.execute(sql)
years_2_json = mycursor.fetchone()
years_2 = json.dumps(years_2_json)
years_2 = years_2.replace("[", "")
years_2 = years_2.replace("]", "")
years_2 = int(years_2)
print(years_2)

#Lấy dữ liệu tổng số ứng dụng và năm cách đây 6 năm
sql="SELECT COUNT(*) as app_number FROM `google_play_apps_data_sample_1` WHERE year(`Date_launch`) <= YEAR(CURDATE() - INTERVAL 6 YEAR)"
mycursor.execute(sql)
All_apps_1_json = mycursor.fetchone()
All_apps_1 = json.dumps(All_apps_1_json)
All_apps_1 = All_apps_1.replace("[", "")
All_apps_1 = All_apps_1.replace("]", "")
All_apps_1 = int(All_apps_1)
print(All_apps_1)
sql="SELECT year(`Date_launch`) as year FROM `google_play_apps_data_sample_1` WHERE year(`Date_launch`) = YEAR(CURDATE() - INTERVAL 6 YEAR) LIMIT 0,1"
mycursor.execute(sql)
years_1_json = mycursor.fetchone()
years_1 = json.dumps(years_1_json)
years_1 = years_1.replace("[", "")
years_1 = years_1.replace("]", "")
years_1 = int(years_1)
print(years_1)
Year = [years_6,years_5,years_4,years_3,years_2,years_1]
Apps = [All_apps_6,All_apps_5,All_apps_4,All_apps_3,All_apps_2,All_apps_1]


sql="select count(App_id) from `google_play_apps_data_sample_1`"
mycursor.execute(sql)
All_apps = mycursor.fetchone()
All_apps_json = json.dumps(All_apps)
All_apps_json = All_apps_json.replace("[", "")
All_apps_json = All_apps_json.replace("]", "")
print(int(All_apps_json))
plt.plot(Year, Apps, color='red', marker='o')
plt.title('Số lượng ứng dụng hiện tại: ' + All_apps_json, fontsize=16)
plt.xlabel('Năm')
plt.ylabel('Số lượng ứng dụng')
plt.grid(True,color='#ffcc29')
# file name   
file_name = 'Line_Chart.png'
# change the current working
# directory
os.chdir("E:/NT114/app/static/")
my_path = os.path.abspath(file_name)
plt.savefig(my_path, transparent=True)