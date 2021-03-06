import os
import json
from flask import Flask, render_template
from sql import Page
app = Flask(__name__)


@app.route('/query/<query>', methods=['GET'])
def simple_query(query):
    return json.dumps([{'book': p[0], 'page': p[1]} for p in Page.search(query)])


@app.route('/')
def render_home():
    return render_template('home.html')


if __name__ == '__main__':
    app.debug = False
    try:
        PORT = int(os.getenv('PORT'))
    except IndexError:
        PORT = 80
    app.run(host='0.0.0.0', port=PORT)
