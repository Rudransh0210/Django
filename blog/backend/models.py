from django.db import models

# Create your models here.
class backend(models.Model):

    name = models.TextField()
    title = models.TextField()
    content = models.TextField()
    s = models.AutoField(primary_key=True)


    def __str__(self) -> str:
        return str(self.s)