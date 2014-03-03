import json
from flask import Flask, abort, Response, render_template
from sql import Page
app = Flask(__name__)


@app.route('/query/<query>', methods=['GET'])
def simple_query(query):
    return json.dumps([{'book': p[0], 'page': p[1]} for p in Page.search(query)])


@app.route('/')
def render_home():
    return render_template('home.html')


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')