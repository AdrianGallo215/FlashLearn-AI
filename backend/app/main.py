from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

cors.init_app(app)

from .routes import upload 

@app.route('/')
def hello_world():
    return "<p>Hello world</p>"

if __name__ == '__main__':
    app.run(debug=True)