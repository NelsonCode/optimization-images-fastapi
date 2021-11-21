from fastapi import FastAPI
from routes.files import routes_files

app = FastAPI()

app.include_router(routes_files)