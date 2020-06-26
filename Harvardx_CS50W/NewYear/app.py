import datetime

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/newyear")
def newyear():
    now = datetime.datetime.now()
    answer = now.month == 1 and now.day == 1 
    return render_template('newyear.html', answer=answer)

@app.route('/res', methods=["POST"])
def res():
    name = request.form.get('value')
    print(name)
    if name == 'no':
        return render_template('help.html', name=name)
    else:
        return render_template('index.html')
if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5001', debug=True)