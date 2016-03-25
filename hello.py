from flask import render_template,Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('hello.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=80)
