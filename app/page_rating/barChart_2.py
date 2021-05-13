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
#Thống kê lượng đánh giá 1 sao theo lượt tải
sql="select count(*) from `google_play_apps_data_sample_1` WHERE (`Downloads` LIKE '%1 - 500%') AND (`Rating_value` <= 1.0);"
mycursor.execute(sql)
One_star_apps_1_json = mycursor.fetchone()
One_star_apps_1 = json.dumps(One_star_apps_1_json)
One_star_apps_1 = One_star_apps_1.replace("[", "")
One_star_apps_1 = One_star_apps_1.replace("]", "")
One_star_apps_1=int(One_star_apps_1)
print(One_star_apps_1)

sql="select count(*) from `google_play_apps_data_sample_1` WHERE (`Downloads` LIKE '%500 - 5000%') AND (`Rating_value` <= 1.0);"
mycursor.execute(sql)
One_star_apps_2_json = mycursor.fetchone()
One_star_apps_2 = json.dumps(One_star_apps_2_json)
One_star_apps_2 = One_star_apps_2.replace("[", "")
One_star_apps_2 = One_star_apps_2.replace("]", "")
One_star_apps_2=int(One_star_apps_2)
print(One_star_apps_2)

sql="select count(*) from `google_play_apps_data_sample_1` WHERE (`Downloads` LIKE '%5000 - 50000%') AND (`Rating_value` <= 1.0);"
mycursor.execute(sql)
One_star_apps_3_json = mycursor.fetchone()
One_star_apps_3 = json.dumps(One_star_apps_3_json)
One_star_apps_3 = One_star_apps_3.replace("[", "")
One_star_apps_3 = One_star_apps_3.replace("]", "")
One_star_apps_3=int(One_star_apps_3)
print(One_star_apps_3)

sql="select count(*) from `google_play_apps_data_sample_1` WHERE (`Downloads` LIKE '%50000 - 5000000%') AND (`Rating_value` <= 1.0);"
mycursor.execute(sql)
One_star_apps_4_json = mycursor.fetchone()
One_star_apps_4 = json.dumps(One_star_apps_4_json)
One_star_apps_4 = One_star_apps_4.replace("[", "")
One_star_apps_4 = One_star_apps_4.replace("]", "")
One_star_apps_4=int(One_star_apps_4)
print(One_star_apps_4)


#Thống kê lượng đánh giá 1-2 sao theo lượt tải
sql5="select count(*) from `google_play_apps_data_sample_1` WHERE (`Downloads` LIKE '%1 - 500%') AND (`Rating_value` > 1.0 AND `Rating_value` <= 2.0);"
mycursor.execute(sql5)
Two_star_apps_1_json = mycursor.fetchone()
Two_star_apps_1 = json.dumps(Two_star_apps_1_json)
Two_star_apps_1 = Two_star_apps_1.replace("[", "")
Two_star_apps_1 = Two_star_apps_1.replace("]", "")
Two_star_apps_1=int(Two_star_apps_1)
print(Two_star_apps_1)

sql6="select count(*) from `google_play_apps_data_sample_1` WHERE (`Downloads` LIKE '%500 - 5000%') AND (`Rating_value` > 1.0 AND `Rating_value` <= 2.0);"
mycursor.execute(sql6)
Two_star_apps_2_json = mycursor.fetchone()
Two_star_apps_2 = json.dumps(Two_star_apps_2_json)
Two_star_apps_2 = Two_star_apps_2.replace("[", "")
Two_star_apps_2 = Two_star_apps_2.replace("]", "")
Two_star_apps_2=int(Two_star_apps_2)
print(Two_star_apps_2)

sql7="select count(*) from `google_play_apps_data_sample_1` WHERE (`Downloads` LIKE '%5000 - 50000%') AND (`Rating_value` > 1.0 AND `Rating_value` <= 2.0);"
mycursor.execute(sql7)
Two_star_apps_3_json = mycursor.fetchone()
Two_star_apps_3 = json.dumps(Two_star_apps_3_json)
Two_star_apps_3 = Two_star_apps_3.replace("[", "")
Two_star_apps_3 = Two_star_apps_3.replace("]", "")
Two_star_apps_3=int(Two_star_apps_3)
print(Two_star_apps_3)

sql8="select count(*) from `google_play_apps_data_sample_1` WHERE (`Downloads` LIKE '%50000 - 5000000%') AND (`Rating_value` > 1.0 AND `Rating_value` <= 2.0);"
mycursor.execute(sql8)
Two_star_apps_4_json = mycursor.fetchone()
Two_star_apps_4 = json.dumps(Two_star_apps_4_json)
Two_star_apps_4 = Two_star_apps_4.replace("[", "")
Two_star_apps_4 = Two_star_apps_4.replace("]", "")
Two_star_apps_4=int(Two_star_apps_4)
print(Two_star_apps_4)

#Thống kê lượng đánh giá 2-3 sao theo lượt tải
sql9="select count(*) from `google_play_apps_data_sample_1` WHERE (`Downloads` LIKE '%1 - 500%') AND (`Rating_value` > 2.0 AND `Rating_value` <= 3.0);"
mycursor.execute(sql5)
Three_star_apps_1_json = mycursor.fetchone()
Three_star_apps_1 = json.dumps(Three_star_apps_1_json)
Three_star_apps_1 = Three_star_apps_1.replace("[", "")
Three_star_apps_1 = Three_star_apps_1.replace("]", "")
Three_star_apps_1=int(Three_star_apps_1)
print(Three_star_apps_1)

sql10="select count(*) from `google_play_apps_data_sample_1` WHERE (`Downloads` LIKE '%500 - 5000%') AND (`Rating_value` > 2.0 AND `Rating_value` <= 3.0);"
mycursor.execute(sql6)
Three_star_apps_2_json = mycursor.fetchone()
Three_star_apps_2 = json.dumps(Three_star_apps_2_json)
Three_star_apps_2 = Three_star_apps_2.replace("[", "")
Three_star_apps_2 = Three_star_apps_2.replace("]", "")
Three_star_apps_2=int(Three_star_apps_2)
print(Three_star_apps_2)

sql11="select count(*) from `google_play_apps_data_sample_1` WHERE (`Downloads` LIKE '%5000 - 50000%') AND (`Rating_value` > 2.0 AND `Rating_value` <= 3.0);"
mycursor.execute(sql7)
Three_star_apps_3_json = mycursor.fetchone()
Three_star_apps_3 = json.dumps(Three_star_apps_3_json)
Three_star_apps_3 = Three_star_apps_3.replace("[", "")
Three_star_apps_3 = Three_star_apps_3.replace("]", "")
Three_star_apps_3=int(Three_star_apps_3)
print(Three_star_apps_3)

sql12="select count(*) from `google_play_apps_data_sample_1` WHERE (`Downloads` LIKE '%50000 - 5000000%') AND (`Rating_value` > 2.0 AND `Rating_value` <= 3.0);"
mycursor.execute(sql8)
Three_star_apps_4_json = mycursor.fetchone()
Three_star_apps_4 = json.dumps(Three_star_apps_4_json)
Three_star_apps_4 = Three_star_apps_4.replace("[", "")
Three_star_apps_4 = Three_star_apps_4.replace("]", "")
Three_star_apps_4=int(Three_star_apps_4)
print(Three_star_apps_4)


#Thống kê lượng đánh giá 3-4 sao theo lượt tải
sql5="select count(*) from `google_play_apps_data_sample_1` WHERE (`Downloads` LIKE '%1 - 500%') AND (`Rating_value` > 3.0 AND `Rating_value` <= 4.0);"
mycursor.execute(sql5)
Four_star_apps_1_json = mycursor.fetchone()
Four_star_apps_1 = json.dumps(Four_star_apps_1_json)
Four_star_apps_1 = Four_star_apps_1.replace("[", "")
Four_star_apps_1 = Four_star_apps_1.replace("]", "")
Four_star_apps_1=int(Four_star_apps_1)
print(Four_star_apps_1)

sql6="select count(*) from `google_play_apps_data_sample_1` WHERE (`Downloads` LIKE '%500 - 5000%') AND (`Rating_value` > 3.0 AND `Rating_value` <= 4.0);"
mycursor.execute(sql6)
Four_star_apps_2_json = mycursor.fetchone()
Four_star_apps_2 = json.dumps(Four_star_apps_2_json)
Four_star_apps_2 = Four_star_apps_2.replace("[", "")
Four_star_apps_2 = Four_star_apps_2.replace("]", "")
Four_star_apps_2=int(Four_star_apps_2)
print(Four_star_apps_2)

sql7="select count(*) from `google_play_apps_data_sample_1` WHERE (`Downloads` LIKE '%5000 - 50000%') AND (`Rating_value` > 3.0 AND `Rating_value` <= 4.0);"
mycursor.execute(sql7)
Four_star_apps_3_json = mycursor.fetchone()
Four_star_apps_3 = json.dumps(Four_star_apps_3_json)
Four_star_apps_3 = Four_star_apps_3.replace("[", "")
Four_star_apps_3 = Four_star_apps_3.replace("]", "")
Four_star_apps_3=int(Four_star_apps_3)
print(Four_star_apps_3)

sql8="select count(*) from `google_play_apps_data_sample_1` WHERE (`Downloads` LIKE '%50000 - 5000000%') AND (`Rating_value` > 3.0 AND `Rating_value` <= 4.0);"
mycursor.execute(sql8)
Four_star_apps_4_json = mycursor.fetchone()
Four_star_apps_4 = json.dumps(Four_star_apps_4_json)
Four_star_apps_4 = Four_star_apps_4.replace("[", "")
Four_star_apps_4 = Four_star_apps_4.replace("]", "")
Four_star_apps_4=int(Four_star_apps_4)
print(Four_star_apps_4)

#Thống kê lượng đánh giá 4-5 sao theo lượt tải
sql5="select count(*) from `google_play_apps_data_sample_1` WHERE (`Downloads` LIKE '%1 - 500%') AND (`Rating_value` > 4.0 AND `Rating_value` <= 5.0);"
mycursor.execute(sql5)
Five_star_apps_1_json = mycursor.fetchone()
Five_star_apps_1 = json.dumps(Five_star_apps_1_json)
Five_star_apps_1 = Five_star_apps_1.replace("[", "")
Five_star_apps_1 = Five_star_apps_1.replace("]", "")
Five_star_apps_1=int(Five_star_apps_1)
print(Five_star_apps_1)

sql6="select count(*) from `google_play_apps_data_sample_1` WHERE (`Downloads` LIKE '%500 - 5000%') AND (`Rating_value` > 4.0 AND `Rating_value` <= 5.0);"
mycursor.execute(sql6)
Five_star_apps_2_json = mycursor.fetchone()
Five_star_apps_2 = json.dumps(Five_star_apps_2_json)
Five_star_apps_2 = Five_star_apps_2.replace("[", "")
Five_star_apps_2 = Five_star_apps_2.replace("]", "")
Five_star_apps_2=int(Five_star_apps_2)
print(Five_star_apps_2)

sql7="select count(*) from `google_play_apps_data_sample_1` WHERE (`Downloads` LIKE '%5000 - 50000%') AND (`Rating_value` > 4.0 AND `Rating_value` <= 5.0);"
mycursor.execute(sql7)
Five_star_apps_3_json = mycursor.fetchone()
Five_star_apps_3 = json.dumps(Five_star_apps_3_json)
Five_star_apps_3 = Five_star_apps_3.replace("[", "")
Five_star_apps_3 = Five_star_apps_3.replace("]", "")
Five_star_apps_3=int(Five_star_apps_3)
print(Five_star_apps_3)

sql8="select count(*) from `google_play_apps_data_sample_1` WHERE (`Downloads` LIKE '%50000 - 5000000%') AND (`Rating_value` > 4.0 AND `Rating_value` <= 5.0);"
mycursor.execute(sql8)
Five_star_apps_4_json = mycursor.fetchone()
Five_star_apps_4 = json.dumps(Five_star_apps_4_json)
Five_star_apps_4 = Five_star_apps_4.replace("[", "")
Five_star_apps_4 = Five_star_apps_4.replace("]", "")
Five_star_apps_4=int(Five_star_apps_4)
print(Five_star_apps_4)
all_One_star_apps=One_star_apps_1+ One_star_apps_2+ One_star_apps_3+ One_star_apps_4
all_Two_star_apps=Two_star_apps_1 + Two_star_apps_2 + Two_star_apps_3 + Two_star_apps_4
all_Three_star_apps=Three_star_apps_1 + Three_star_apps_2 + Three_star_apps_3 + Three_star_apps_4
all_Four_star_apps=Four_star_apps_1 + Four_star_apps_2 + Four_star_apps_3 + Four_star_apps_4
all_Five_star_apps=Five_star_apps_1 + Five_star_apps_2 + Five_star_apps_3 + Five_star_apps_4
category_names = ['<500', '500-5000','5000-50000', '>50000']
results = {
    '0 - 1.0': [One_star_apps_1/all_One_star_apps, One_star_apps_2/all_One_star_apps, One_star_apps_3/all_One_star_apps, One_star_apps_4/all_One_star_apps],
    '1.0 - 2.0': [Two_star_apps_1/all_Two_star_apps, Two_star_apps_2/all_Two_star_apps, Two_star_apps_3/all_Two_star_apps, Two_star_apps_4/all_Two_star_apps],
    '2.0 - 3.0': [Three_star_apps_1/all_Three_star_apps, Three_star_apps_2/all_Three_star_apps, Three_star_apps_3/all_Three_star_apps, Three_star_apps_4/all_Three_star_apps],
    '3.0 - 4.0': [Four_star_apps_1/all_Four_star_apps, Four_star_apps_2/all_Four_star_apps, Four_star_apps_3/all_Four_star_apps, Four_star_apps_4/all_Four_star_apps],
    '4.0 - 5.0': [Five_star_apps_1/all_Five_star_apps, Five_star_apps_2/all_Five_star_apps, Four_star_apps_3/all_Five_star_apps, Four_star_apps_4/all_Five_star_apps]
}
def survey(results, category_names):
    labels = list(results.keys())
    data = np.array(list(results.values()))
    data_cum = data.cumsum(axis=1)
    category_colors = plt.get_cmap('RdYlGn')(
        np.linspace(0.15, 0.85, data.shape[1]))

    fig, ax = plt.subplots(figsize=(9.2, 5))
    ax.invert_yaxis()
    ax.xaxis.set_visible(False)
    ax.set_xlim(0, np.sum(data, axis=1).max())

    for i, (colname, color) in enumerate(zip(category_names, category_colors)):
        widths = data[:, i]
        starts = data_cum[:, i] - widths
        rects = ax.barh(labels, widths, left=starts, height=0.5,
                        label=colname, color=color)
        plt.ylabel("ĐIỂM ĐÁNH GIÁ")
        r, g, b, _ = color
        text_color = 'white' if r * g * b < 0.5 else 'darkgrey'
        #ax.bar_label(rects, label_type='center', color=text_color)
    ax.legend(ncol=len(category_names), bbox_to_anchor=(0, 1),
              loc='lower left', fontsize='small')
    return fig, ax
survey(results, category_names)
file_name = 'RATING_APPS_2.png'
# change the current working
# directory
os.chdir("E:/NT114/app/static/")
my_path = os.path.abspath(file_name)
plt.savefig(my_path, transparent=True)
