from flask import Flask, render_template
app = Flask(__name__)
@app.route('/play/')
def playGround():
    return render_template('index.html', num = 3, color = 'hsl(214.38deg 86.41% 79.8%)' )

@app.route('/play/<num>')
def playGroundNum(num):
    return render_template('index.html', num = int(num), color = 'hsl(214.38deg 86.41% 79.8%)')

@app.route('/play/<num>/<color>')
def playGroundColor(num, color):
    return render_template('index.html', num = int(num), color = color)

if __name__ =="__main__":
    app.run(debug=True)