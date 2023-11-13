from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def main():
    return render_template('index.html',x=8, y = 8, color1 = 'red', color2 = 'blue')
@app.route('/<y>')
def main_y(y):
    return render_template('index.html',x=8, y = y, color1 = 'red', color2 = 'blue')
@app.route('/<y>/<x>')
def main_yx(y,x):
    return render_template('index.html',x=int(x), y = int(y), color1 = 'red', color2 = 'blue')
@app.route('/<y>/<x>/<color1>/<color2>')
def main_yx_color(y,x,color1,color2):
    return render_template('index.html',x=int(x), y = int(y), color1 = str(color1), color2 = str(color2))
if __name__=="__main__":
    app.run(debug=True)    