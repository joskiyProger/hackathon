from fastapi import FastAPI, Request, Form, Query, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
# from sqlalchemy import create_engine, Column, Integer, String
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker, Session
# from databases import Database

# DATABASE_URL = "postgresql://myuser:mypassword@localhost/mydatabase"

# # Создание базы данных для асинхронных операций
# database = Database(DATABASE_URL)

# # Создание SQLAlchemy ORM модели
# Base = declarative_base()

# class User(Base):
#     __tablename__ = "Users"
    
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, index=True)
    
app = FastAPI()   

# @app.on_event("startup")
# async def startup():
#     await database.connect()

# @app.on_event("shutdown")
# async def shutdown():
#     await database.disconnect()


app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "argument": "jinja argument"})

@app.get("/success", response_class=HTMLResponse)
async def success(request: Request, username: str = Query(...), password: str = Query(...)):
    print(username, password)
    return templates.TemplateResponse("base.html", {"argument": f"{username}, {password}", "request": request})
    # return {"name": username, "password": password, "request": request}

@app.post("/submit")
async def loginPostReqest(username:str = Form(), password: str = Form()):
    if (str(username) == "qwe" and str(password) == "123"):
        # print(username)
        # return {"ok": 123}
        return RedirectResponse(url=f"/success?username={username}&password={password}", status_code=303)
    return {"error": "not valid"}


# @app.post("/add_user/")
# async def create_book(name: str):
#     query = Users.__table__.insert().values(name=name)
#     last_record_id = await database.execute(query)
#     return {"id": last_record_id}


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