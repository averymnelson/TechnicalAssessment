import strawberry
from .app import Query, Mutation, CheckFav
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

schema = strawberry.Schema(Query, Mutation, CheckFav)
graphql_app = GraphQLRouter(schema)

app=FastAPI()
app.include_router(graphql_app, prefix="/graphql")