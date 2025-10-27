from djongo import models

class Team(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=100, unique=True)

class User(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

class Activity(models.Model):
    _id = models.ObjectIdField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    duration = models.IntegerField()

class Workout(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=100)
    description = models.TextField()

class Leaderboard(models.Model):
    _id = models.ObjectIdField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    points = models.IntegerField()
