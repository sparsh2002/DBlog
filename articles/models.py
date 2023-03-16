from django.db import models

# run these commands as you update this file
# python manage.py makemigrations
# python manage.py migrate

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    # add in thumbnail later
    # add in author late

    def __str__(self):
        return self.title



