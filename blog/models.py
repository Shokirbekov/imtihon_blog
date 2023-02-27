from django.db import models
from django.contrib.auth.models import User

class Muallif(models.Model):
    ism = models.CharField(max_length=50)
    yosh = models.PositiveIntegerField()
    kasb = models.TextField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.ism

class Maqola(models.Model):
    sarlavha = models.CharField(max_length=500)
    sana = models.DateField(auto_now_add=True)
    mavzu = models.TextField()
    matn = models.TextField()
    muallif = models.ForeignKey(Muallif, on_delete=models.CASCADE)
    def __str__(self):
        return self.sarlavha