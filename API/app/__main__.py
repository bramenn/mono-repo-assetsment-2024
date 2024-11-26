import uvicorn
from fastapi import FastAPI

from .cultivo import endpoint as cultivo_endpoint
from .db import Base, conn
from .evento import endpoint as evento_endpoint

app = FastAPI(root_path="/api")

app.include_router(cultivo_endpoint.router, prefix="/v1/cultivo", tags=["cultivo"])
app.include_router(evento_endpoint.router, prefix="/v1/evento", tags=["evento"])


if __name__ == "__main__":
    Base.metadata.create_all(conn)
    uvicorn.run(app=app, host="0.0.0.0", port=80)
