# TO RUN THE SERVER, RUN "FLASK --APP SERVER_FILE_NAME run --debug"
# debug mode will reload the server every time there's a update in any file
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")