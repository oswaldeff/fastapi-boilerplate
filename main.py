
from datetime import datetime

from fastapi import FastAPI
from fastapi.responses import JSONResponse

# FastAPI APP
app = FastAPI(
    debug=True,
    title="fastapi-boilerplate",
    description="보일러플레이트 코드",
    version="0.0.1",
    terms_of_service="",
    dependencies=None,
    default_response_class=JSONResponse,
    doc_url='/docs',
    redoc_url='/redoc',
    openapi_url=None,
    openapi_tags=[],
    openapi_prefix="",
    contact={
        "github": "https://github.com/oswaldeff",
        "email": "tialem94@gmail.com",
    },
    license_info=None,
)

@app.on_event("startup")
async def startup_event():
    datetime_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("server_log.txt", mode="a") as log: # 로그이외의 다른 알림형태로 대체
        log.write(f"\n Application startup, {datetime_now}")

@app.on_event("shutdown")
async def shutdown_event():
    datetime_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("server_log.txt", mode="a") as log: # 로그이외의 다른 알림형태로 대체
        log.write(f"\n Application shutdown, {datetime_now}")
