from django.db import models

" CREATE TABLE posts (id not null primary key autoincrement, title text, body text, rate int)"

class Post(models.Model):
    title = models.CharField(max_length=256)
    content = models.CharField(max_length=456)
    rate = models.IntegerField(default=0, null=True)

    def __str__(self):
        return f"{self.title} - {self.content}"
