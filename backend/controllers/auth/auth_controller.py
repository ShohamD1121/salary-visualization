# from fastapi import FastAPI, Depends, HTTPException, APIRouter
# from fastapi.security import OAuth2PasswordBearer
# from authlib.integrations.starlette_client import OAuth
# from dotenv import load_dotenv
# import os

# load_dotenv()

# router = APIRouter()
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

# oauth = OAuth()
# auth0 = oauth.register(
#     "auth0",
#     client_id=os.getenv("CLIENT_ID", "null"),
#     client_secret=os.getenv("CLIENT_SECRET", "null"),
#     server_metadata_url=os.getenv("AUTH0_DOMAIN", ""),
#     client_kwargs={"scope": "openid profile email"},
# )

# # Function to get the current user (dependency)


# async def get_current_user(token: str = Depends(oauth2_scheme)):
#     user = None
#     try:
#         user = auth0.parse_id_token(token)
#     except Exception as e:
#         raise HTTPException(status_code=401, detail="Invalid token")
#     return user


# # Example protected endpoint
# @router.get("/protected")
# async def protected_endpoint(user=Depends(get_current_user)):
#     return {"message": f"Hello, {user['name']}!"}
