import os
from flask import render_template, Flask
from flask import send_from_directory

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('hello.html')


@app.route('/build/react.js')
def react():
    return send_from_directory(os.path.join(app.root_path, 'build'), 'react.js')


@app.route('/app.js')
def appjs():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'app.js')


@app.route('/build/react-dom.js')
def reactdom():
    return send_from_directory(os.path.join(app.root_path, 'build'), 'react-dom.js')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
