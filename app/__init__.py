from flask import Flask
from flask import Flask

app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True)

import app.routes as routes