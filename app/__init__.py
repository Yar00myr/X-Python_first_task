from os import getenv
from flask import Flask
from dotenv import load_dotenv
from flask_wtf.csrf import CSRFProtect

load_dotenv()
SECRET_KEY = getenv("SECRET_KEY")

app = Flask(__name__)
app.config["SECRET_KEY"] = SECRET_KEY
csrf = CSRFProtect(app)


from . import routes


if __name__ == "__main__":
    app.run(port=5000)
