from django.db import models
from django.forms import model_to_dict

# Create your models here.

class User_story(models.Model):
    actor = models.CharField(max_length=200, verbose_name='Actor', default='Quien')
    accion = models.CharField(max_length=500, verbose_name='Accion', default='Que')
    proposito = models.CharField(max_length=500, verbose_name='Proposito', default='Para que')
    dificultad = models.PositiveIntegerField(default=0)

    def __str__(self):
        return '{} {} {}'.format(self.actor, self.accion, self.proposito)


    class Meta:
        verbose_name = 'Historia de Usuario'
        verbose_name_plural = 'Historias de Usuario'
        db_table = 'historia'
        ordering = ['id']


class Auxiliar(models.Model):
    relatoUsuario = models.CharField(max_length=1000, verbose_name='Historia')

    def __str__(self):
        return '{}'.format('Historia')

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Relato del Usuario'
        verbose_name_plural = 'Relatos'
        db_table = 'cuento'
        ordering = ['id']



class Accion(models.Model):
    actor = models.CharField(max_length=300, verbose_name='Actor')
    que = models.CharField(max_length=1000, verbose_name='Que')
    para_que = models.CharField(max_length=1000, verbose_name='Para_que')
    posicion = models.PositiveIntegerField()
    aux = models.ForeignKey(Auxiliar, on_delete=models.CASCADE, verbose_name='Auxiliar')

    def __str__(self):
        return "Quien: {} Como: {} Para que: {}".format(self.actor, self.que, self.para_que)

    def toJSON(self):
        item = model_to_dict(self)
        item['aux'] = self.aux.toJSON()
        return item

    class Meta:
        verbose_name = 'Accion'
        verbose_name_plural = 'Acciones'
        db_table = 'accion'
        ordering = ['id']

