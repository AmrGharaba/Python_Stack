from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route('/')
def survey():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    print(request.form)
    name = request.form['name']
    location = request.form['location']
    favorite_language = request.form['favorite_language']
    comment = request.form['comment']
    return render_template('result.html', name = name, location = location, favorite = favorite_language, comment = comment )


if __name__=='__main__':
    app.run(debug=True)