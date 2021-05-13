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

sql="select count(App_id) from `google_play_apps_data_sample_1`"
mycursor.execute(sql)
All_apps = mycursor.fetchone()
All_apps_json = json.dumps(All_apps)
All_apps_json = All_apps_json.replace("[", "")
All_apps_json = All_apps_json.replace("]", "")
All_apps_json = int(All_apps_json)
print(All_apps_json)
category_names = ['1', '2','3', '4', '5']
results = {
    '': [Rating_1_json, Rating_2_json, Rating_3_json, Rating_4_json, Rating_5_json]
}
Average_Rating_apps = (Rating_1_json+Rating_2_json*2+Rating_3_json*3+Rating_4_json*4+Rating_5_json*5)/All_apps_json
Average_Rating_apps = round(Average_Rating_apps,1)
def survey(results, category_names):
    labels = list(results.keys())
    data = np.array(list(results.values()))
    data_cum = data.cumsum(axis=1)
    category_colors = plt.get_cmap('RdYlGn')(
        np.linspace(0.15, 0.85, data.shape[1]))

    fig, ax = plt.subplots(figsize=(10, 0.8))
    ax.invert_yaxis()
    ax.xaxis.set_visible(False)
    ax.set_xlim(0, np.sum(data, axis=1).max())

    for i, (colname, color) in enumerate(zip(category_names, category_colors)):
        widths = data[:, i]
        starts = data_cum[:, i] - widths
        ax.barh(labels, widths, left=starts, height=0.2,
                label=colname, color=color)
        xcenters = starts + widths / 2

        r, g, b, _ = color
        text_color = 'black'
        for y, (x, c) in enumerate(zip(xcenters, widths)):
            ax.text(x, y, str(int(c)), ha='center', va='center',
                    color=text_color)
    ax.legend(ncol=len(category_names), bbox_to_anchor=(0, 0),
              loc='upper left', fontsize='15')
    return fig, ax
survey(results, category_names)
file_name = 'bar_Chart.png'
# change the current working
# directory
os.chdir("E:/NT114/app/static/")
my_path = os.path.abspath(file_name)
plt.savefig(my_path, transparent=True)
