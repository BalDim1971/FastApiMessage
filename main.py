from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse

from routers import users, messages

app = FastAPI()

# Добавляем роутеры для пользователей и сообщений.
app.include_router(users.router)
app.include_router(messages.router)


@app.get("/")
async def read_root():
    return {"message": "Приложение работает!"}


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail},
    )


if __name__ == '__main__':
    import uvicorn
    
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        log_level="info",
        reload=True)
