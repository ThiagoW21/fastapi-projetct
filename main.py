from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.infra.sqlalchemy.config.data_base import create_bd
from src.routes import routes_contribuitors, routes_items, routes_auth


create_bd()


app = FastAPI()

origins = ["*",
    "http://localhost:3000/",
    "http://inventary-v1.herokuapp.com/me",
    ]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

# Routes Security

app.include_router(routes_auth.router)

# Router Contribuitors

app.include_router(routes_contribuitors.router)


# Routes Items

app.include_router(routes_items.router)
