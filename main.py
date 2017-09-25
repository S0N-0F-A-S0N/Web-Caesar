from flask import Flask, request

app = Flask(__name__)
app.config['DEBUG'] = True


form = ''.join(open('web-caesar.html', 'r').readlines())

@app.route("/")
def index():
    return form

@app.route("/path/", methods=['POST']) # this is the path that will be returned.
def path():
    fname = request.form['first']
    return "<h1> Hi there, " + fname + """</h1>
<p> How are you? </p>
"""

app.run()
