from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return render_template('hello.html', message='Hello World')

@app.route('/<string:name>', methods=['GET'])
def get_name(name):
    return render_template('hello.html', message='Hello %s' % name)

if __name__ == '__main__':
    app.run()