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


class Link(models.Model):
    label = models.CharField(max_length=100)
    url = models.URLField()
    public = models.BooleanField(default=True, help_text='Visible to anonymous visitors. If false, only shown to logged-in users.')
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order', 'label']

    def __str__(self):
        return self.label
