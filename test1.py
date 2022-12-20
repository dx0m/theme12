from flask import Flask, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'abc'
@app.post('/auth')
def auth():
    session['auth'] = request.form.to_dict()['user']
    return redirect(url_for('main'))

@app.route("/")
def main():
    if 'auth' not in session:
        return '<form action="/auth" metod ="post"><input name = "user"><input type = "submit"></form>'
    else:
        u = session['auth']
        return f'Hello, {u}'