import uvicorn
from fastapi import FastAPI

from .cultivo import endpoint as cultivo_endpoint
from .db import Base, conn

app = FastAPI()

app.include_router(cultivo_endpoint.router, prefix="/v1/cultivo", tags=["cultivo"])


if __name__ == "__main__":
    Base.metadata.create_all(conn)
    uvicorn.run(app=app, host="0.0.0.0", port=5000)
