from flask import render_template,Flask,request
from page_index.lineChart import *
from page_index.pieChart import *
from page_index.barChart import *
from page_freevspaid.barChart import *
from page_rating.barChart_1 import *
from page_rating.barChart_2 import *
#xu ly khi ban vao host 127.0.0.1:5000
app = Flask(__name__)

@app.route('/')
def index ():
    to_send=str(Average_Rating_apps)
    to_send1=str(int(Average_Rating_apps*20))+"%"
    return render_template('index.html',Average_Rating=to_send, percent_rating=to_send1) #se hien ra giao dien la file index.html

@app.route('/freevspaid', methods=['GET', 'POST'])
def freevspaid ():
    to_send=str(Average_Rating_apps)
    to_send1=str(int(Average_Rating_apps*20))+"%"
    # show the form, it wasn't submitted
    return render_template('freevspaid.html',Average_Rating=to_send, percent_rating=to_send1)

@app.route('/rating', methods=['GET', 'POST'])
def rating ():
    to_send=str(Average_Rating_apps)
    to_send1=str(int(Average_Rating_apps*20))+"%"
    # show the form, it wasn't submitted
    return render_template('rating.html',Average_Rating=to_send, percent_rating=to_send1)
if __name__ == "__main__":
    app.run()