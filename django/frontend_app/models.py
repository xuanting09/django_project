from django.db import models

class ExampleModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title


from django.db import models

class SecurityNews(models.Model):
    title = models.CharField(max_length=255)
    publish_date = models.DateField()
    url = models.URLField(unique=True)
    content_summary = models.TextField()
    content = models.TextField()

    def __str__(self):
        return self.title
