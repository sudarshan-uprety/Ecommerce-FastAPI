from typing import Union
from fastapi import FastAPI, Request, HTTPException,Depends
from database import *
from modles import *

app = FastAPI()


@app.get("/")
def read_root():
    return ("Hey welcome to my Ecommerce-FastAPI project.")


@app.post("/createAccount")
async def create_account(request: Request):
    data = await request.json()
    try:
        if not all(data.values()):
            raise HTTPException(
                status_code=400, detail="fields can not be empty")

        if data["password"] != data["confirm_password"]:
            raise HTTPException(
                status_code=400, detail="Password can confirm password fields do not match.")
        db_disconnect()
        db_connection()

        user = User(email=data["email"], first_name=data["first_name"],
                    last_name=data["last_name"], phone=data["phone"])
        user.set_password(data["password"])
        user.save()
        raise HTTPException()

    except NotUniqueError:
        raise HTTPException(status_code=400, detail="Email already exist.")
    except Exception:
        raise HTTPException(status_code=400, detail="Something went wrong.")
