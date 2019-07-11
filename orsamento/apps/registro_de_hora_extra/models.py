from django.db import models
from apps.funcionarios.models import funcionarios


class Registro_De_Horas_Extra(models.Model):
    motivo = models.CharField(max_length=70)
    funcionario = models.ForeignKey(funcionarios,on_delete=models.PROTECT)

    def __str__(self):
        return self.motivo