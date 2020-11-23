from flask import Flask, render_template, request, session
from datetime import datetime
import os
app = Flask(__name__)
#app.secret_key = os.environ['SESSION_KEY'] todo: fix for production
app.secret_key = b'\xaf\t\xd9\xbaZU\x02\x19\xc8\xbb\xf3\xdc\x1d\xb9~\xb4'

@app.route('/',  methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        print(request.form)
        session['username'] = request.form['username']

    if 'username' in session:
        current_day = datetime.now().day
        clicked_dict = dict()
        line_ragna_ns = ['172468', '172469', '172477', '172898', '173272']
        anders_ns = ['173393', '173394', '173446', '173511', '173517']
        siva_ns = ['173516', '173733', '173696', '173682', '173764']
        gorel_ns = ['174368', '174371', '174380', '174390', '174392']
        annika_ns = ['174437', '174439', '174441', '174442']
        #nettskjema_ids = line_ragna_ns + anders_ns + siva_ns + gorel_ns + annika_ns
        nettskjema_ids = ['174371','173764', '173733', '174380', '173696', '174439', '173517', '173446', '172469', '173516', '174392', '173682', '174437', '173511', '172468', '174390', '173272', '173394', '173393', '172898', '174442', '172477', '174368', '174441']
        if 'clicked_date' in session:
            clicked_dict = session['clicked_date']
        return render_template('calendar.html', username = session['username'], current_day=current_day, clicked_dict = clicked_dict, nettskjema_ids=nettskjema_ids)
    else:
        return render_template('getusername.html')

@app.route('/receivedata', methods=['POST'])
def receive_data():
    clicked_date = request.form['clicked_date']
    if 'clicked_date' not in session:#
        session['clicked_date'] = dict()
    session['clicked_date'][clicked_date]='clicked'
    session.modified = True
    return 'ok'