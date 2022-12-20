from flask import Flask, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'key'

@app.post('/message')
def message():
    session['message'] = request.form.to_dict()['mess']
    return redirect(url_for('main'))

@app.route('/')
def main():
    count_1 = 0
    if 'auth' not in session:
        return '<form action="/message" metod="post"><input name = "mess"><input type = "submit"></form>'
    else:
        u = session['auth']
        count_1 = count_1 + 1
        return f'<h>{u}{count}</h>'