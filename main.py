from typing import List
from fastapi import FastAPI
# import connection
from database import database as connection
#import models
from database import User
from database import Movie
from database import UserReview

# import schemas
from schemas import UserRequestModel
from schemas import UserResponseModel


app = FastAPI(title='Proyecto para reseñar peliculas',
description='En este proyecto reseñaremos peliculas',
version='1')

# events
@app.on_event('startup')
def startup():
  if connection.is_closed():
    connection.connect()
    print('Connecting ...')
  # create tables
  connection.create_tables({User, Movie, UserReview})
  print('Servidor iniciado')

@app.on_event('shutdown')
def shutdown():
  if not connection.is_closed():
    connection.close()
    print('Closing ...')
  print('El servidor finalizo')

# requests
@app.get('/')
async def index():
  return 'Hola mundo desde fastapi'

@app.get('/about')
async def about():
  return 'About'

@app.post('/users')
# usaremos el BaseModel para indicar que datos y tipos necesitamos
async def create_user(user_data: UserRequestModel):
  hash_password = User.create_password(user_data.password)
  new_user = User.create(
    username= user_data.username,
    password= hash_password
  )
  return new_user.id

@app.get('/users/', response_model=List[UserResponseModel])
async def get_users():
  users = User.select()
  return [ user for user in users ]
