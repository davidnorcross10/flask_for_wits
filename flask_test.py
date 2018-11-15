from flask import Flask, render_template, request
from pyscripts import wits
app = Flask(__name__)

data = wits.url_formatter("swz","2000","wld","all","XPRT-TRD-VL")
countryList = wits.returnJSON('/home/david/Documents/Flask_test/static/country_codes_json.txt')
@app.route("/")
@app.route("/home")
def hello():
    return render_template('home.html',data=data[0],url=data[1])
    #"<h2>Home Page</h2>"
    #render_template(home.html)

@app.route("/graphs",methods=["GET","POST"])
def graphs():
    return render_template('graphs.html',data=data[0],url=data[1],countryList=countryList)
    #"<h2>Home Page</h2>"
    #render_template(home.html)

@app.route("/about")
def about():
    return "<h2>About Page</h2>"
