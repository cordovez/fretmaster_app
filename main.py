from fastapi import FastAPI
import uvicorn


from routes.client_side_routes import front_router
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(front_router, tags=["app"])


if __name__ == "__main__":
    uvicorn.run(reload=True, app="main:app")
