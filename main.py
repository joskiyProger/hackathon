from fastapi import FastAPI, Request, Form, Query, Depends, Response
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from datetime import datetime
import uuid
from fastapi.exceptions import HTTPException
import smtplib
from email.mime.text import MIMEText
import hashlib
import passlib
from passlib.context import CryptContext

app = FastAPI()

OWN_EMAIL = "kChudinovv@yandex.ru"
OWN_EMAIL_PASSWORD = "abfojocivtpcdoqc"


def send_email(message: str):
    try:
        msg = MIMEText(message, "plain", "utf-8")
        # msg['Subject'] = "Добавление нового сотрудника"
        # msg['From'] = f'Denolyrics <{OWN_EMAIL}>'
        # msg['To'] = "k_chudinovv@mail.ru"

        port = 587
        server = smtplib.SMTP("smtp.yandex.ru", port, timeout=10)
        
        server.starttls()
        print(OWN_EMAIL, OWN_EMAIL_PASSWORD)
        
        server.login(OWN_EMAIL, OWN_EMAIL_PASSWORD)
        
        server.sendmail(OWN_EMAIL, "k_chudinovv@mail.ru", msg.as_string())
        
        server.quit()
        return {"message": "Email sent successfully"}

    except Exception as e:
        error_data = {
            "error": "Failed to send email",
            "details": str(e)
        }
        return error_data

# @app.post("/email")
# def send_email(message: str):
#     try:
#         msg = MIMEText(message)
#         msg['Subject'] = "Добвление нового сотрудника"
#         # msg['From'] = f'Denolyrics <{OWN_EMAIL}>'
#         # msg['To'] = body.to

#         print(1)
#         port = 587
#         server = smtplib.SMTP_SSL("smtp.gmail.com", port)
        
#         print(2)
#         server.starttls()
#         server.login(OWN_EMAIL, OWN_EMAIL_PASSWORD)
#         server.sendmail(OWN_EMAIL, "k_chudinovv@mail.ru", msg.as_string())
#         server.quit()
#         return {"message": "Email sent successfully"}

#     except Exception as e:
#         # return {"error": "unknown"}
#         error_data = {
#             "error": "Failed to send email",
#             "details": str(e)
#         }
#         return error_data
#         raise HTTPException(status_code=500, detail=e)
    


app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.post("/loginPost", response_class=HTMLResponse)
async def loginPost(request: Request, response : Response, password: str = Form(), login:str = Form()):
    if login == "123" and password == "123": # надо будет сделать проверку с данными из бд
        response = RedirectResponse(url=f"/personalAccount", status_code=303)
        uid = uuid.uuid4()
        response.set_cookie(key="uid", value=str(uid))
        response.set_cookie(key="admin_rights", value=1)
        # по логину обратиться в бд и в поле юид запихнуть юид кторый я тут засунул в куки
        return response
    else:
        return templates.TemplateResponse("login.html", {"request": request, "valid_status": "Неверное имя пользователя или пароль!"})   
    
@app.get("/", response_class=HTMLResponse)
async def index(request: Request, response : Response):
    response = templates.TemplateResponse("login.html", {"request": request})
    response.delete_cookie("uid")
    response.set_cookie(key="admin_rights", value=0)
    return response


@app.get("/leaderboard", response_class=HTMLResponse)
async def leaderboard(request: Request, response : Response):
    if request.cookies.get("uid"):
        response = templates.TemplateResponse("leaderboard.html", {"request": request})
        return response
    else: 
        return RedirectResponse(url=f"/", status_code=303)


@app.get("/personalAccount", response_class=HTMLResponse)
async def personalAccount(request: Request, response : Response):
    if request.cookies.get("uid"):
        response = templates.TemplateResponse("personal_account.html", {"request": request})
        return response
    else: 
        return RedirectResponse(url=f"/", status_code=303)


@app.get("/success", response_class=HTMLResponse)
async def success(response : Response, request: Request, username: str = Query(...), password: str = Query(...)):
    # print(send_email("test msg"))
    return templates.TemplateResponse("base.html", {"argument": f"{username}, {password}", "request": request})

@app.post("/submit")
async def submit(response : Response,  username:str = Form(), password: str = Form()):
    if (str(username) and str(password) == "123"):
        uid = uuid.uuid4()
        password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        hashed_password = password_context.hash(password)
        hashed_user = password_context.hash(username)
        # h.update(username.encode())
        # hashed_user = h.hexdigest()
        print(hashed_password, hashed_user)
        print(password_context.verify(password, hashed_password))
        response = RedirectResponse(url=f"/success?username={username}&password={password}", status_code=303)
        response.set_cookie(key="uid", value=str(uid))
        return response
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