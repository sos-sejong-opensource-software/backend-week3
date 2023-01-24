from django.db import models
import uuid

# Create your models here.

class TodoModel(models.Model):
    """ Model definition for Todo"""
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    is_starred = models.BooleanField()
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now_add=True)

    # class Meta:
    #     db_table = "todos"
