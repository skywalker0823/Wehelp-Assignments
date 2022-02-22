
from multiprocessing import connection
import os
import re
from flask import *
from flask import request
from flask import render_template as rt
from flask import redirect
from flask import session
import pymysql
from dbutils.pooled_db import PooledDB
from dotenv import load_dotenv
from flask import jsonify
from cerberus import Validator

load_dotenv()

POOL = PooledDB(
    creator=pymysql,  # Which DB module to use
    maxconnections=6,  # Allowed max connection, 0 and None means no limitations.
    mincached=2,  # Least connection when created, 0 means don't.
    blocking=True,  # Queue when there is no connection avaliable. True = wait；False = No waits, and report error.
    ping=0, # Check if Mysql service is avaliable # if：0 = None = never, 1 = default = whenever it is requested, 2 = when a cursor is created, 4 = when a query is executed, 7 = always

    host='127.0.0.1',
    port=3306,
    user='root',
    password=os.getenv("DB_PASS"),
    database='website',
    charset='utf8',
    cursorclass=pymysql.cursors.DictCursor
)
connection = POOL.connection()
# connection=pymysql.connect(charset='utf8',db='website',host='127.0.0.1',password='',port=3306,user='root')

app=Flask(__name__,
static_folder="public",
static_url_path="/"
)

app.secret_key=os.getenv("SECRET_KEY")

@app.route("/")
def login():
    if session.get("username"):
        return redirect("/member")
    else:
        return rt("login.html")

@app.route("/signin", methods=["POST"])
def signin():
    acc=request.form["account"]
    pss=request.form["password"]
    if acc=="" or pss=="":
        return redirect("/error/?message=帳號或密碼不能為空")
    with connection.cursor() as cursor:
        got=cursor.execute("""SELECT * FROM member WHERE username=%s""",(acc,))
        result=cursor.fetchone()
        connection.commit()
        if got==0:
            return redirect("/error/?message=帳號或密碼錯誤")
        elif got==1:
            if pss==result['password']:
                session['username']=[acc,result['name']]
                return redirect("/member")
            else:
                return redirect("/error/?message=帳號或密碼錯誤")
        else:
            return redirect("/error/?message=錯光光")

@app.route("/member")
def member():
    if session.get("username"):
        return rt("member.html",message=session['username'][1]+"恭喜您~成功登入系統:)")
    else:
        return redirect("/")

@app.route("/signup", methods=["POST"])
def register():
    name=request.form["name"]
    username=request.form["username"]
    password=request.form["password"]
    with connection.cursor() as cursor:
        got=cursor.execute("""SELECT * FROM member WHERE username=%s""",(username,))
        connection.commit()
        if got!=0:
            return redirect("/error/?message=帳號已被註冊")
        else:
            with connection.cursor() as cursor:
                result=cursor.execute(
                    """INSERT INTO
                        member(
                            name,
                            username,
                            password)
                    VALUES(%s,%s,%s)""",(name,username,password))
                connection.commit()
                print("註冊完成 新增: ",result,"筆資料")
                return redirect("/")

@app.route("/api/members" , methods=["GET"])
def members():
    username=request.args.get("username")
    with connection.cursor() as cursor:
        got=cursor.execute("""SELECT * FROM member WHERE username=%s""",(username,))
        result=cursor.fetchone()
        connection.commit()
        if got!=0:
            id=result["id"]
            name=result["name"]
            user_name=result["username"]
            summary={"data":{"id":id,"name":name,"username":user_name}}
            return jsonify(summary)
        else:
            return jsonify({"data":None})

@app.route("/api/member" , methods=["POST"])
def change_name():
    schema={'name':{'type':'string'}}
    v=Validator(schema)
    if session.get("username"):
        try: 
            data=request.get_json()
            hell_gate=v.validate(data)
            print("data的樣貌: ", data)
            print("地獄的樣貌: ",hell_gate)
            if data=={}:
                return jsonify({"error":"data is empty"})
        except:
            print("except錯誤")
            return jsonify({"error":"data is not json"})
        else:
            try:
                if hell_gate == False or data["name"] == "":
                    print("Cerberus:錯誤的內容")
                    return jsonify({"error":"denied by Cerberus."})
            except:
                print("內層except錯誤")
                return jsonify({"error":"true"})
            else:
                username=session["username"][0]
                with connection.cursor() as cursor:
                    changed=cursor.execute("""
                            UPDATE member 
                            SET name=%s
                            WHERE username=%s
                    """,(data["name"],username))
                    connection.commit()
                    result={"ok":"true"}
                    session["username"][1]=data["name"]
                    session["username"]=session["username"]
                    return jsonify(result)
    else:
        return jsonify({"error":"true"})

@app.route("/error/")
def error():
    message=request.args.get("message")
    return rt("error.html",message=message)

@app.route('/signout')
def signout():
    print("使用者",session["username"],"登出")
    session["username"]=None
    return redirect("/")

if __name__=="__main__":
    app.run(debug=True, port="3000")
