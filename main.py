from fastapi import Depends, FastAPI, HTTPException, Query, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

import secrets
import os

app = FastAPI()

security = HTTPBasic()


def validate_credentials(credentials: HTTPBasicCredentials = Depends(security)) -> None:
    input_user_name = credentials.username.encode("utf-8")
    input_password = credentials.password.encode("utf-8")

    stored_username = str(os.getenv("USER")).encode()
    stored_password = str(os.getenv("PASSWORD")).encode()

    is_username = secrets.compare_digest(input_user_name, stored_username)
    is_password = secrets.compare_digest(input_password, stored_password)

    if not (is_username and is_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Basic"},
        )


@app.get("/hello")
async def hello(name: str = Query(), _: None = Depends(validate_credentials)) -> dict:
    return {"message": f"Hello, {name}!"}
