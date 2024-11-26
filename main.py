from fastapi import FastAPI, Request, Form, Query
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "result": "jinja argument"})

@app.get("/success", response_class=HTMLResponse)
async def success(username: str = Query(...), password: str = Query(...)):
    print(username, password)
    return templates.TemplateResponse("base.html", {"result": "text"})
    # return {"name": username, "password": password}


@app.post("/")
def loginPostReqest(username=Form(), password=Form()):
    if (str(username) == "qwe" and str(password) == "123"):
        return RedirectResponse(f"/success?username={username}&password={password}")
    return {"error": "not valid"}

# @app.route('/registration', methods=['GET', 'POST'])
# def registration():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         password_confirm = request.form['password_confirm']
#         users = User.query.filter(User.username == username and User.password == password).all()
#         if password == password_confirm and len(users) == 0:
#             new_user = User(username=username, password=password)
#             try:
#                 db.session.add(new_user)
#                 db.session.commit()
#                 return redirect(url_for('main'))
#             except:
#                 return "Чтото пошло не так при создании пользователя :("
#         else:
#             return render_template("reg_pg.html")
#     else:
#         return render_template("reg_pg.html")
    

# @app.route('/', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
        
#         # users = User.query.order_by(User.id).all()
#         users = User.query.filter(User.username == username and User.password == password).all()
#         # if format(request.cookies.get('username')) and format(request.cookies.get('password')):
        
#         if len(users) != 0 and not request.cookies.get('username'):
#             res = make_response(redirect(url_for('main')))
#             res.set_cookie('username', users[0].username, max_age=60*60*24*365*2, secure=True, httponly=True, samesite="strict")
#             res.set_cookie('password', users[0].password, max_age=60*60*24*365*2, secure=True, httponly=True, samesite="strict")
#             return res
#         else:
#             res = make_response(render_template("log_pg.html"))
#             res.set_cookie('username', '', max_age=0)
#             res.set_cookie('password', '', max_age=0)
#             return res
#     else:
#         res = make_response(render_template("log_pg.html"))
#         res.set_cookie('username', '', max_age=0)
#         res.set_cookie('password', '', max_age=0)
#         return res


# @app.route('/main', methods=['GET', 'POST'])
# def main():
#     if request.cookies.get('username') and request.cookies.get('password'): return render_template("index.html")
#     else: return redirect(url_for('login'))

# @app.route('/cookie/')
# def cookie():
#     if not request.cookies.get('foo'):
#         res = make_response("Setting a cookie")
#         res.set_cookie('foo', 'bar', max_age=60*60*24*365*2)
#     else:
#         res = make_response("Value of cookie foo is {}".format(request.cookies.get('foo')))
#     return res


# if __name__ == "__main__":
#     app.run(debug=True)