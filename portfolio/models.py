from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=200)
    codename = models.CharField(max_length=50, blank=True)
    description = models.TextField()
    status = models.CharField(max_length=100, default='Active')
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order', 'title']

    def __str__(self):
        return self.title
