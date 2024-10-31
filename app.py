from flask import Flask,request,render_template as rt
import os

app = Flask(__name__)

@app.route("/check_form.html")
@app.route("/check_form")
def check_form():
    res = request.args
    return rt('check_form.html',res=res)

@app.route("/")
@app.route("/index.html")
@app.route("/index")
def index():
    #print(args)
    #args = os.getenv("API")
    not_needed = ["file.html"]
    data = {}
    """
    data = {
        "links":
            {"/":{"name":"index","id":0},
            "/index":{"name":"index","id":1},
            "/system":{"name":"system","id":2},
            "/walk":{"name":"walk","id":3},
            "/form":{"name":"form","id":4},
            "/login":{"name":"form","id":5}
            },
        "info":{}
        }
    """
    #print(os.listdir(./))
    #links = {f"./{name}":{"name":name,"id":id} for id,name in enumerate(os.listdir("./templates")) if name not in not_needed}
    links = {f"/{name}":{"name":name,"id":id} for id,name in enumerate(os.listdir("./templates")) if name not in not_needed}
    data["links"] = links
    
    return rt('index.html',title="Index",data=data)


@app.route("/system.html")
@app.route("/system")
def system():
    data = {"env":os.environ}
    return rt("system.html",title="System",data=data)


@app.route("/walk")
@app.route("/walk.html")
def walk():
    data = {}
    lst_files = []
    #print(os.walk('/apps'))
    #for l in os.walk("/home/alma/prog"):
    #    print(l)
    #print(os.getcwd())

    for  parent,dnames,fnames in os.walk(os.getcwd()):
        for fname in fnames:
            fpath = os.path.join(parent,fname)
            data[fpath] = fname  
            
    return rt("walk.html",title="Walk",data=data)

@app.route("/<path:path>")
def file(path):
    data = {}
    with open(path) as f:
        for i,l in enumerate(f):
            data[i] = f.readline()
            
    return rt("file.html",title="File",data=data)


@app.route("/form")
@app.route("/form.html")
def form():
    data = {"env":os.environ}
    return rt("form.html",title="Form",data=data)


@app.route("/login.html")
@app.route("/login")
def login():
    data = {}
    return rt("login.html",title="Login",data=data)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)