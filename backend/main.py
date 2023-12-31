from fastapi import FastAPI
from middleware.middleware import setup_middlewares
from controllers.data_processing import router as data_processing_router

# for app starting ---> python -m uvicorn main:app --reload

app = FastAPI()
setup_middlewares(app)
app.include_router(data_processing_router)
