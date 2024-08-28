from django.db import models


class Usuarios(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=30)
    numero = models.TextField(max_length=13)
    senha = models.TextField(max_length=99)

    