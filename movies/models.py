from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255, null=False)
    year = models.IntegerField(null=False)
    director = models.CharField(max_length=100, null=False)
    genre = models.CharField(max_length=100, null=False)
    synopsis = models.TextField()
    picture = models.ImageField(upload_to="movie_images", null=True, blank=True)

    def __str__(self):
        return self.title
