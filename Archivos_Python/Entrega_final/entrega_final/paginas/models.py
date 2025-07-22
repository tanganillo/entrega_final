from django.db import models


class Pagina(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=150)
    image = models.ImageField(upload_to='pages/')
    pub_date = models.DateField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return self.title