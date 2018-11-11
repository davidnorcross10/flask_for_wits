from flask import Flask, render_template
from pyscripts import wits
app = Flask(__name__)

data = [
    {
    "id":"food",
    "value":"20"
    },
    {
    "id":"services",
    "value":"30"
    }
]

data = wits.url_formatter("usa","2000","wld","all","XPRT-TRD-VL")

@app.route("/")
@app.route("/home")
def hello():
    return render_template('home.html',data=data[0],url=data[1])
    #"<h2>Home Page</h2>"
    #render_template(home.html)

@app.route("/graphs")
def graphs():
    return render_template('graphs.html',data=data[0],url=data[1])
    #"<h2>Home Page</h2>"
    #render_template(home.html)

@app.route("/about")
def about():
    return "<h2>About Page</h2>"
