import dbcon
import json
from fastapi import FastAPI, Request, Form, Query, Depends, Response
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from datetime import datetime
import uuid
from fastapi.exceptions import HTTPException
import smtplib
import hashlib
import passlib
from passlib.context import CryptContext


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.post("/loginPost", response_class=HTMLResponse)
async def loginPost(request: Request, response : Response, password: str = Form(), login:str = Form()):
    if dbcon.is_login_valid(login, password):
        response = RedirectResponse(url=f"/personalAccount", status_code=303)
        uid = uuid.uuid4()
        response.set_cookie(key="uid", value=str(uid))
        response.set_cookie(key="admin_rights", value=1)
        dbcon.set_uid(login, uid)
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
    if dbcon.is_uid_exist(request.cookies.get("uid")):
        data = { "request": request } | dbcon.get_all_data()
        return templates.TemplateResponse("leaderboard.html", data)
    else: 
        return RedirectResponse(url=f"/", status_code=303)


@app.get("/personalAccount", response_class=HTMLResponse)
async def personalAccount(request: Request, response : Response):
    if dbcon.is_uid_exist(request.cookies.get("uid")):
        data = { "request": request } | dbcon.get_employee_by_uid(request.cookies.get("uid"))
        return templates.TemplateResponse("personal_account.html", data)
    else: 
        return RedirectResponse(url=f"/", status_code=303)
