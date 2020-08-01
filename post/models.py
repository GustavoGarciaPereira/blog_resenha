from django.db import models

# Create your models here.


class Post(models.Model):
    titulo= models.CharField(max_length=60)
    post=models.TextField()
    data_publicacao=models.DateTimeField(auto_now_add=True)
    imagem_post=models.URLField()

    def __str__(self):
        return self.titulo
    
class Autor(models.Model):
    pass