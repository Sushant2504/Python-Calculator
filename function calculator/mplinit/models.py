from django.db import models

# Create your models here.
class Mplinit(models.Model):
    expr = models.CharField(max_length=150)

    def __str__(self):
        return str(self.expr)

class TNN(models.Model):
    expr = models.CharField(max_length=150)
    x_value = models.CharField(max_length=50)
    def __str__(self):
        return str(self.expr)

class ULLIM(models.Model):
    f = models.CharField(max_length=150)
    g = models.CharField(max_length=150)
    l_lim = models.CharField(max_length=50)
    u_lim = models.CharField(max_length=50) 
    def __str__(self):
        return str(self.f)
    