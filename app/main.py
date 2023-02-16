import typing
import strawberry
import json
import requests

from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

def get_weather(root, city: str):
        base = "https://api.openweathermap.org/data/2.5/weather?"
        key = "7b05635832e5a91f48a7c3ed1eaec35d"
        url = base+"q="+city+"&appid="+key
        response = requests.get(url)
        data1 = response.json()
        main = data1['main']
        tempK = main['temp']
        tempF=(tempK-273.15)*(9/5)+32
        humidity=main['humidity']
        # return "In {city}, the temperature is {tempF:.2f} F and the humidity is {humidity}%."
        return [Weather(city, tempK, tempF, humidity)]

@strawberry.type
class City():
    city: str      
                
@strawberry.type
class Weather():
    city: typing.List[City] = strawberry.field(resolver=get_weather)
    tempK: float
    tempF: float
    humidity: float   
   
@strawberry.type        
class Favorites:
    city: str
    
#come back to check query, feels convoluted
@strawberry.type
class Query:
    cities: typing.List[Weather] = strawberry.field(resolver=get_weather)

@strawberry.type
class Mutation:
    @strawberry.field
    def add_fav(self, city: str) -> Favorites:
        ...
        
@strawberry.type
class CheckFav:
    cities: typing.List[Weather] = strawberry.field(resolver=get_weather)

schema = strawberry.Schema(Query)
graphql_app = GraphQLRouter(schema)

app=FastAPI()
app.include_router(graphql_app, prefix="/graphql")