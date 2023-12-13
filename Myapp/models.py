from email.policy import default
from django.db import models

# Create your models here.


class Lugar(models.Model):
    nombre_lugar=models.CharField(max_length=20)

    def __str__(self):
        return self.nombre_lugar
        

class Colchon(models.Model):
    numero_colchon=models.PositiveIntegerField(primary_key=True)
    lugar=models.ForeignKey(Lugar,default=1 ,null=False, on_delete=models.CASCADE)
    boton=models.BooleanField(default=False)
    def __str__(self):
        x=str(self.numero_colchon)
        l=str(self.lugar)
        return f"{x}-{l}"



class Estudiante(models.Model):
    nombre_estudiante=models.CharField(max_length=50, primary_key=True)
    municipio=models.CharField(max_length=10)
    residencia=models.PositiveIntegerField()
    colchon=models.ForeignKey(Colchon, on_delete=models.CASCADE)

    def __str__(self):

        y=str(self.colchon)
        return  f"{self.nombre_estudiante} - {y}"
