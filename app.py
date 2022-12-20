from flask import Flask, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'abc'
mess = [None,None,None,None]

@app.route('/', methods=['GET', 'POST'])
def authorization():
    global mess
    while request.method == 'POST':
       mess.append(request.form.get('Message'))
       return '''
             <form method="POST">
                 <div><label>Message: <input type="text" name="Message"></label></div>
                 <input type="submit" value="Enter">
                 <div><h1>Четыре последних сообщения:</h1></div>
                 <div>{}</div>
                 <div>{}</div>
                 <div>{}</div>
                 <div>{}</div>
             </form>
             '''.format(mess[-1],mess[-2],mess[-3],mess[-4])

    return '''
             <form method="POST">
                 <div><label>Message: <input type="text" name="Message"></label></div>
                 <input type="submit" value="Enter">
             </form>
             '''