from flask import Flask, render_template, url_for, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    title = 'Moj site'
    return render_template('test.html', title=title)


@app.route('/data')
def data():
    my_data = {
        'profile': 'Mario',
        'badges': ['one', 'two', 'tree'],
    }

    return jsonify(my_data)

if __name__ == '__main__':
    app.run()
