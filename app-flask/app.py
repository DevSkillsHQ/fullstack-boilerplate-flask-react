from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

@app.route('/ping')
def hello_world():
    return 'ok'

if __name__ == '__main__':
    app.run()
