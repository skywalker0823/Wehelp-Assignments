from flask import *
from flask import request
from flask import render_template as rt
from flask import redirect
from flask import session
import pymysql

connection=pymysql.connect(charset='utf8',db='website',host='127.0.0.1',password='',port=3306,user='root',cursorclass=pymysql.cursors.DictCursor)

app=Flask(__name__,
static_folder="public",
static_url_path="/"
)

app.secret_key="1234"

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
        return rt("member.html",message=session['username'][1]+"，恭喜您，成功登入系統:)")
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
