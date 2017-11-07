from flask import Flask
from flask import render_template
import os

app = Flask(__name__)


@app.route('/', defaults={'path': '/'})
@app.route('/<path:path>')
def hello_world(path):
    return render_template('index.html',
                           envs=os.environ,
                           path=path)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
