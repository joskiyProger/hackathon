import dbcon
import json
from fastapi import FastAPI, Request, Form, Query, Depends, Response
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from datetime import datetime
import uuid
from fastapi.exceptions import HTTPException


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


def collect_request_info(request: Request):
    request_info = {
        "client_host": request.client.host,
        "client_port": request.client.port,
        "method": request.method,
        "url": str(request.url)
    }
    return request_info


@app.post("/resetTransactionsData", response_class=JSONResponse)
async def loginPost(password: str = Form()):
    if password == "123":
        dbcon.reset_all_transactions()
        return {"message": "data restored"}
    else:
        return {"message": "permission denied"}


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


@app.get("/login", response_class=HTMLResponse)
async def login(request: Request, response : Response):
    response = templates.TemplateResponse("login.html", {"request": request})
    response.delete_cookie("uid")
    response.set_cookie(key="admin_rights", value=0)
    return response


@app.get("/")
async def leaderboard(request: Request, response : Response):
    if dbcon.is_uid_exist(request.cookies.get("uid")):
        request_info = collect_request_info(request)
        full_info = {"request_info": request_info} | dbcon.get_all_data() 
        return JSONResponse(content=full_info) 
    else:
        return RedirectResponse(url=f"/login", status_code=303)


@app.get("/personalAccount", response_class=HTMLResponse)
async def personalAccount(request: Request, response : Response):
    if dbcon.is_uid_exist(request.cookies.get("uid")):
        request_info = collect_request_info(request)
        full_info = {"request_info": request_info} | dbcon.get_employee_by_uid(request.cookies.get("uid"))
        return JSONResponse(content=full_info) 
    else: 
        return RedirectResponse(url=f"/", status_code=303)
