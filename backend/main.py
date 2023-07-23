from fastapi.responses import HTMLResponse
from fastapi import FastAPI
from middleware.middleware import setup_middlewares
from controllers.data_processing import router as data_processing_router
from fastapi.openapi.docs import get_swagger_ui_html

# for app starting ---> python -m uvicorn main:app --reload

app = FastAPI()
setup_middlewares(app)
app.include_router(data_processing_router)


@app.get("/docs", response_class=HTMLResponse)
async def get_documentation():
    return get_swagger_ui_html(openapi_url="/openapi.json", title="API Documentation")
