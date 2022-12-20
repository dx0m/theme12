from flask import Flask, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'abc'

@app.route('/', methods=['GET', 'POST'])
def authorization():
    mess = []
    while request.method == 'POST':
       mess.append(request.form.get('Message'))
       return '''
             <form method="POST">
                 <div><label>Message: <input type="text" name="Message"></label></div>
                 <input type="submit" value="Enter">
                 <div>{}</div>
             </form>
             '''.format(mess[0])

    return '''
             <form method="POST">
                 <div><label>Message: <input type="text" name="Message"></label></div>
                 <input type="submit" value="Enter">
             </form>
             '''