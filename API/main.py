import os
from fastapi import FastAPI, Response, APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/os-info")
def os_info():
    payload = {
        "cpu_count": os.cpu_count(),
    }
    return JSONResponse(content=payload, status_code=200)


@router.get("/hello")
def hello():
    payload: dict = {
        "message": "Hello, World!",
        "author": "Nadeem",
    }
    Response = JSONResponse(content=payload, status_code=200)
    Response.headers["X-Custom-Header"] = "Custom Header"
    return Response

app = FastAPI()
app.include_router(router)
