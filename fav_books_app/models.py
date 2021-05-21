from django.db import models
from django.db.models.fields import related
from login_registration_app.models import *

# Create your models here.
class BookManager(models.Manager):
    def validator(self, postData):
        errors = {}

        if not postData['title']:
            errors['title'] = "A title is required"

        if len(postData['desc']) < 5:
            errors['desc'] = "The description should be longer than 5 characters"

        return errors

class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    uploaded_by = models.ForeignKey(User, related_name="uploaded_books", on_delete=models.CASCADE)
    users_who_like = models.ManyToManyField(User, related_name="favorited_books")
    objects = BookManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)