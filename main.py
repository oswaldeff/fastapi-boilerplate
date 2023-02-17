
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

@app.get("/")
async def root():
    return {"message": "Hello World"}
