from peewee import *
from datetime import datetime

database = MySQLDatabase('fastapi', user='root', password='', host='localhost', port=3306)


#models

class User(Model):
  username = CharField(max_length=50, unique=True)
  password = CharField(max_length=50)
  created_at = DateTimeField(default=datetime.now)

  def __str__(self):
    return self.username

  class Meta:
    # se hace referencia al objeto database creado en la linea 4
    database = database
    table_name = 'users'

class Movie(Model):
  title = CharField(max_length=50)
  created_at = DateTimeField(default=datetime.now)

  def __str__(self):
    return self.title

  class Meta:
    # se hace referencia al objeto database creado en la linea 4
    database = database
    table_name = 'movies'

class UserReview(Model):
  user = ForeignKeyField(User, backref='reviews')
  user = ForeignKeyField(Movie, backref='reviews')
  review = TextField()
  score = IntegerField()
  created_at = DateTimeField(default=datetime.now)

  def __str__(self):
    return f'{self.user.username} - {self.movie.title}'

  class Meta:
    # se hace referencia al objeto database creado en la linea 4
    database = database
    table_name = 'user_reviews'
