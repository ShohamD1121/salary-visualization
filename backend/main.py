from fastapi import FastAPI, Depends, Response, status
from fastapi.security import HTTPBearer
from middleware.middleware import setup_middlewares
from controllers.data_processing import router as data_processing_router
# from controllers.auth.auth_controller import router as auth_router
from utils.utils import VerifyToken

# for app starting ---> python -m uvicorn main:app --reload

app = FastAPI()
setup_middlewares(app)
app.include_router(data_processing_router)
# app.include_router(auth_router)


token_auth_scheme = HTTPBearer()


@app.get("/api/public")
def public():
    """No access token required to access this route"""

    result = {
        "status": "success",
        "msg": ("Hello from a public endpoint! "
                "You don't need to be authenticated to see this.")
    }
    return result


@app.get("/api/private")
def private(response: Response, token: str = Depends(token_auth_scheme)):
    """A valid access token is required to access this route"""

    result = VerifyToken(token.credentials).verify()

    if result.get("status"):
        response.status_code = status.HTTP_400_BAD_REQUEST
        return result

    return result
