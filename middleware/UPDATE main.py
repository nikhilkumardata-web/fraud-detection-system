from fastapi import FastAPI
from app.routes.transaction import router
from app.middleware.timing import timing_middleware

app = FastAPI()

app.middleware("http")(timing_middleware)
app.include_router(router)

@app.get("/")
def home():
    return {"message": "Fraud Detection System Running"}
