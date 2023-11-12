from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World!'
@app.route('/<name>')
def dojo(name):
    return name.title() + '!'
@app.route('/say/<name>')
def say(name):
    return f'Hi {name} !'
@app.route('/repeat/<num>/<str>')
def repeat(num, str):
    strs = ''
    for i in range (int(num)):
        strs+=f'\n{str.title()}'
    return strs
if __name__=="__main__":
    app.run(debug=True)