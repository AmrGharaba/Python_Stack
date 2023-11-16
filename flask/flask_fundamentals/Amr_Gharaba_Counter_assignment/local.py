from flask import Flask,render_template, redirect, request,session
app = Flask(__name__)
app.secret_key = '123'
@app.route('/')
def index():
    if 'count' in session:
        session['count'] +=1
    else:
        session['count'] = 0
    return render_template('index.html', count = session['count'])

@app.route('/reset',methods = ['POST'])
def reset():
    session['count'] = 0
    return redirect('/')

@app.route('/plus2',methods = ['POST'])
def plus2():
    session['count'] += 1
    return redirect('/')

if __name__ == '__main__':  
    app.run(debug = True)