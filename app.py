from flask import Flask
from flask import render_template
import os

app = Flask(__name__)


@app.route('/', defaults={'path': '/'})
@app.route('/<path:path>')
def hello_world(path):
    envs = os.environ
    if os.getenv("ENV_WHITELIST"):
        whitelist = os.getenv("ENV_WHITELIST").split(",")
        envs = {k: v for (k, v) in envs.items() if k in whitelist}
    return render_template('index.html',
                           envs=envs,
                           path=path)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
