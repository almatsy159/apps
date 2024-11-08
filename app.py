from flask import Flask,request,render_template as rt
import os
import glob
import re
from modules.logger import logger as lg
import mysql.connector as mc
import setting as s
app = Flask(__name__)

@app.route("/check_form.html")
@app.route("/check_form")
def check_form():
    res = request.args
    lg.output(res,prfx="check_form")
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
    lg.output(data,prfx="index")
    
    return rt('index.html',title="Index",data=data)


@app.route("/system.html")
@app.route("/system")
def system():
    data = {"env":os.environ}
    lg.output(data,prfx="system")
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
    lg.output(data,prfx="file")
    return rt("file.html",title="File",data=data)


@app.route("/form")
@app.route("/form.html")
def form():
    data = {"env":os.environ}
    lg.output(data,prfx="form")
    return rt("form.html",title="Form",data=data)


@app.route("/login.html")
@app.route("/login")
def login():
    data = {}
    lg.output(data,prfx="login")
    return rt("login.html",title="Login",data=data)

@app.route("/tools")
@app.route("/tools.html",methods = ["POST"])
@app.route("/tools.html")
def tools():
    #print(fname)
    #print(request.form)
    fname = request.form.get("fname")
    print(fname)
    #fname = req[0]
    tools = get_tools()
    #print(args)
    if fname != None:
        #fname = args["fname"]  
        print("fname",fname)
        if fname == "":
            res = "empty file name"
        elif fname in tools:
            #res = exec(fname)
            print(f"tools.{fname} should be executed see the result at static/output.txt")
            exec(f"import {f'tools.{fname}'}")
            with open("static/output.txt","r") as f:
                res = f.readlines()
            
        else :
            res = "file not found"
    else :
        res = "no args"
    
    data = {"tools":tools,"res":res}
    
    lg.output(data,prfx="tools")
    
    return rt("tools.html",title="Tools",data=data)

@app.route("/inscription")
def inscription():
    return "hi"


@app.route("/db")
def db(table=""):
    
    db = mc.Data
    if table == "":
        req = "SHOWS TABLES;"
    else :
        req = f"SELECT * FROM {table};"
        
    c = mc.cursor()
    c.execute(req)
    data = c.fetchall()
    c.close()
    
    return rt("db.html",table=table)

#g(f)  or g(f(x))
def wrapper(f,lst):
    #before
    res = f(lst)
    #after
    return res
    


def get_tools():
    fpath = glob.glob("tools/*.py")
    res = []
    for f in fpath:
        res.append(get_name_from_path(f))
    return res
    
def get_name_from_path(path):
    pattern = re.compile(r"(\w*\/)*(\w*).py")
    res = re.findall(pattern,path)
    #print(res)
    res = res[0][1]
    return res

class DB:
    def __init__(self,user=s.LOGIN,pwd=s.PWD,host=s.HOST,db=s.DB):
        self.db = db
        self.user = user
        self.host = host
        self.connect(pwd)
        #self.struct = self.struct_db()
        #print(self.struct)
        
    def connect(self,pwd,user=None):
        if user == None:
            user = self.user
        self.conn = mc.connect(user=user,host=self.host,passwd=pwd,database=self.db)
    
    def commit(self):
        self.conn.commit()
    def make_req(self,req="select * from program;"):
        cursor = self.conn.cursor()
        cursor.execute(req)
        res = cursor.fetchall()
        # trt single many here 
        #self.commit()
        cursor.close()
        if res != []:
            print(req,"=>",res)
        else : 
            print(req)
        return res
    
    def struct_db(self):
        res =""
        i1 = f"USE {self.db}"
        self.make_req(i1)
        i2 = "SHOW TABLES"
        
        tables = self.make_req(i2)
        res = {}
        for t in tables:
            #print(t[0])
            res[t] = []
            i3 = f"SHOW COLUMNS from {t[0]};"
            cols = self.make_req(i3)
            res[t].append(cols)
            
        return res
            
    
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)