from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def table():
    return render_template('index.html', users = users)

@app.route('/<first_name>/<last_name>')
def table1(first_name,last_name):
    
    users.append({'first_name':first_name, 'last_name':last_name})
    return render_template('index.html', users = users)

users = [
    {'first_name' : 'Michael', 'last_name' : 'Choi'},
    {'first_name' : 'John', 'last_name' : 'Supsupin'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

if __name__=='__main__':
    app.run(debug=True)