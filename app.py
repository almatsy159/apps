from flask import Flask,render_template as rt
import os

app = Flask(__name__)

@app.route("/")
def index():
    #print(args)
    args = os.getenv("API")
    return rt('index.html',args=args)


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=3000,debug=True)