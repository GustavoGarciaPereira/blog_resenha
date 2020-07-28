from django.db import models

# Create your models here.



class Post(models.Model):
    titulo = models.CharField(max_length=30)
    post = models.TextField()
    data_publicacao = models.DateTimeField(auto_now_add=True)
    imagem_post = models.URLField(max_length=200)

class Autor(models.Model):
    pass
    