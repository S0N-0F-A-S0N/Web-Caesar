from flask import Flask, request
from caesar import encrypt

app = Flask(__name__)
app.config['DEBUG'] = True


form = ''.join(open('web-caesar.html', 'r').readlines())

@app.route("/")
def index():
    return form.format("")

@app.route("/path/", methods=['POST']) # this is the path that will be returned.
def path():
    rotation = request.form['rot']
    message = request.form['text']
    return form.format(encrypt(str(message), int(rotation)))

app.run()
