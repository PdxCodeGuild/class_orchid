from django.db import models

# Create your models here.

'''
Movie <-> Director
Many-to-one

Movie <-> Actor
many-to-many
'''


class Director(models.Model):
    '''
    The primary key from this table will be in the 'director' column of the Movie table
    'director_instance.movie_set' refers to this director's movies
    'director_instance.movie_set.all()' gets all of them
    'director_instance.movie_set.create(title="totally rad movie")' creates a new movie with this director on it
    '''
    name = models.CharField(max_length=70)

    def __str__(self):
        return self.name


class Movie(models.Model):
    '''
    'movie_instance.actor_set.all()' gets all actors associated with this movie
    'movie_instance.actor_set.add(actor_instance)' creates an association between actor and movie
    'movie_instance.actor_set.create(name="Mr. Guy")' creates (and saves) a new instance of Actor associated with this movie
    '''
    title = models.CharField(max_length=500)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Actor(models.Model):
    '''
    'actor_instance.movies.all()' gets all actors associated with this movie
    'actor_instance.movies.add(movie_instance)' creates an association between actor and movie
    'actor_instance.movies.create(title="totally rad movie 2: the reckoning", director=director_instance)' 
        creates (and saves) a new instance of Movie associated with this actor
    '''
    name = models.CharField(max_length=70)
    movies = models.ManyToManyField(Movie)  # doesn't have to be set at first!

    def __str__(self):
        return self.name
