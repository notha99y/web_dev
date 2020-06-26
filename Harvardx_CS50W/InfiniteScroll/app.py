import time

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/posts', methods = ["POST"])
def posts():
    '''Get more posts'''
    
    start = int(request.form.get('start') or 0)
    end = int(request.form.get('end') or (start+9))
    data = []
    for i in range(start, end+1):
        data.append(f'Post #{i}')
    
    # Act like loading
    time.sleep(1)

    return jsonify(data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port = '5001')