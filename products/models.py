from django.db import models
from django.contrib.auth.models import User

class Products(models.Model):
    title=models.CharField(max_length=100)
    date=models.DateTimeField()
    url=models.CharField(max_length=200)
    body=models.TextField()
    image=models.ImageField(upload_to='image/')
    icon=models.ImageField(upload_to='image/')
    upvote=models.IntegerField(default=1)
    hunter=models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:100]
    
    def date_pretty(self):
        return self.date.strftime('%b %e %Y')