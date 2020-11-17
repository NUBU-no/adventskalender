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
        if 'clicked_date' in session:
            clicked_dict = session['clicked_date']
        return render_template('calendar.html', username = session['username'], current_day=current_day, clicked_dict = clicked_dict)
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