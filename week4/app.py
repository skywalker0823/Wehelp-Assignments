from email import message
from flask import *
from flask import request
from flask import render_template as rt
from flask import redirect
from flask import session

app=Flask(__name__,
static_folder="public",
static_url_path="/"
)

app.secret_key="1234"

@app.route("/")#首頁->登入與註冊
def login():
    print("有客人來囉")
    if session.get("user"):
        return redirect("/member")#已登入者自動導向
    else:
        return rt("login.html")

@app.route("/signin", methods=["POST"])#登入意圖
def signin():
    acc=request.form["account"]
    pss=request.form["password"]
    if acc=="" or pss=="":
        return redirect("/error?message=帳號或密碼不能為空")
    elif acc=="test" and pss=="test":#驗證成功 紀錄session
        session['user']=acc
        return redirect("/member")
    else:
        return redirect("/error?message=帳號或密碼錯誤")
    
    

@app.route("/member")#主頁
def member():
    if session.get("user"):
        print(session['user'],"來到首頁")
        return rt("member.html",message="恭喜您，成功登入系統:)")
    else:
        print("未知使用者嘗試存取主頁")
        return redirect("/")

@app.route("/error")#錯誤頁面->錯誤方式產生訊息變化
def error():
    message=request.args.get("message")
    return rt("error.html",message=message)

@app.route('/signout')#登出意圖
def signout():
    print("使用者",session["user"],"登出")
    session["user"]=None
    return redirect("/")


if __name__=="__main__":
    app.run(debug=True, port="3000")
