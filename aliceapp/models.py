from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

class Poll(models.Model):
    question = models.TextField()
    answer1 = models.CharField(max_length=500)
    answer2 = models.CharField(max_length=500)
    image1 = models.ImageField(upload_to='images/')
    image2 = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.question