from django.db import models
from apps.funcionarios.models import funcionarios


class documento(models.Model):
    descricao = models.CharField(max_length=70)
    pertence = models.ForeignKey(funcionarios, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.descricao