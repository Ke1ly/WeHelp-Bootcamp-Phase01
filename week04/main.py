from fastapi import FastAPI, Request,Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from urllib.parse import quote
from starlette.middleware.sessions import SessionMiddleware

app=FastAPI()
templates = Jinja2Templates(directory="templates")

app.mount("/static",StaticFiles(directory="static"),name="static")

app.add_middleware(SessionMiddleware, secret_key="jv;rghi;w5ijnm")

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/signin")
async def signin(request: Request,account: str = Form(...), password: str = Form(...)):
    if not account or not password:
        message=quote("Please enter username and password")
        return RedirectResponse(url=f"/error?message={message}", status_code=303)
    elif password=="test" and account=="test":
        request.session["SIGNED-IN"]=True
        return RedirectResponse(url="/member", status_code=303)
    else:
        message=quote("Username or password is not correct")
        return RedirectResponse(url=f"/error?message={message}", status_code=303)


@app.get("/member")
def memberget(request: Request):
    if not request.session.get("SIGNED-IN", False) or request.session["SIGNED-IN"]==False:
        return RedirectResponse(url="/", status_code=303)
    else:
        return templates.TemplateResponse("member.html", {"request": request})

@app.get("/error")
def error(request: Request,message):
    return templates.TemplateResponse("error.html", {"request": request,"message":message})

@app.get("/square/{number}")
async def square(number, request: Request):
    number=int(number)
    return templates.TemplateResponse("square.html",{"request": request,"square":number*number})

@app.get("/signout")
async def signout(request: Request):
    request.session.clear()
    request.session["SIGNED-IN"]=False
    return RedirectResponse(url="/", status_code=303)

