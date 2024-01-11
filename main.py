from fastapi import FastAPI
import uvicorn


from routes.client_side_routes import front_router

app = FastAPI()


app.include_router(front_router, prefix="/app", tags=["app"])


if __name__ == "__main__":
    uvicorn.run(reload=True, app="server:app")
