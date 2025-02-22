from fastapi import FastAPI, Request, Form, Depends, Response
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from urllib.parse import quote
import mysql.connector
import os
from typing import Generator
from starlette.middleware.sessions import SessionMiddleware


def get_db() -> Generator:
    try:
        con = mysql.connector.connect(
       user = os.getenv("MYSQL_USER"),
    password = os.getenv("MYSQL_PASSWORD"),
    host = os.getenv("MYSQL_HOST"),
    database = os.getenv("MYSQL_DATABASE")
    )
        yield con
    except mysql.connector.Error as e:
        print(f"資料庫連線錯誤: {e}")
    finally:
        con.close() 

app=FastAPI()
templates = Jinja2Templates(directory="templates")

app.mount("/static",StaticFiles(directory="static"),name="static")

app.add_middleware(SessionMiddleware, secret_key="jve5jnm84i,")

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html",{"request":request})

@app.post("/signup")
async def signup(request: Request, username = Form(...), name=Form(...), password=Form(...),db=Depends(get_db)):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM member WHERE username=%s",(username,))
    result = cursor.fetchone()
    if result:
        message=quote("sign up failed: repeated username")
        return RedirectResponse(url=f"/error?message={message}", status_code=303)
    else:
        cursor.execute("INSERT INTO member(name, username, password) VALUES (%s, %s, %s)",(name, username, password))
        db.commit()
        cursor.close()
        return RedirectResponse(url="/", status_code=303)

@app.post("/signin")
async def signup(request: Request, username = Form(...), password=Form(...), db=Depends(get_db)):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM member WHERE username=%s AND password=%s",(username, password))
    result = cursor.fetchone()
    cursor.close()
    if result:
        request.session["SIGNED-IN"]=True
        request.session["username"]=username
        request.session["name"]=result[1]
        request.session["id"]=result[0]
        return RedirectResponse(url="/member", status_code=303)
    else:
        message=quote("username or password is not correct")
        return RedirectResponse(url=f"/error?message={message}", status_code=303)


@app.get("/member")
async def member(request: Request, db=Depends(get_db)):
        if not request.session.get("SIGNED-IN"):
            return RedirectResponse(url="/", status_code=303)
        else:
            cursor = db.cursor(dictionary=True)
            cursor.execute("SELECT member.name, message.content, message.member_id, message.id FROM message INNER JOIN member ON message.member_id=member.id;")
            messages = cursor.fetchall()
            name = request.session.get("name")
            member_id = request.session.get("id")
            cursor.close()
            return templates.TemplateResponse("member.html", {"request": request,"name":name,"messages":messages,"member_id":member_id})

@app.get("/signout")
async def signout(request: Request):
    request.session.clear()
    return RedirectResponse(url="/", status_code=303)

@app.get("/error")
async def error(request: Request, message):
    return templates.TemplateResponse("error.html", {"request": request,"message":message})

@app.post("/createMessage")
async def createMessage(request: Request, message = Form(...), db=Depends(get_db)):
    id = request.session.get("id")
    cursor = db.cursor()
    cursor.execute("INSERT INTO message(member_id, content)VALUES(%s,%s)",(id,message))
    db.commit()
    cursor.close()
    return RedirectResponse(url="/member", status_code=303)

@app.post("/deleteMessage/{message_id}")
async def deleteMessage(request: Request , message_id:int, db=Depends(get_db)):
    cursor = db.cursor()
    cursor.execute("DELETE FROM message WHERE id=%s",(message_id,))
    db.commit()
    cursor.close()
    return Response(status_code=200)