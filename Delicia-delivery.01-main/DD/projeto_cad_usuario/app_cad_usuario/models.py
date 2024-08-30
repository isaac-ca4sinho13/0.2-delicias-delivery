from django.db import models


class Usuarios(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=30)
    numero = models.TextField(max_length=13)
    senha = models.TextField(max_length=99)


class Vendedor(models.Model):
    id_vendedor = models.AutoField(primary_key=True)
    pass

class Comida(models.Model):
    id_comida = models.AutoField(primary_key = True)

class Pedidos(models.Model):
    id_Comida = models.ForeignKey(Comida)
    id_Usuario = models.ForeignKey(Usuarios)