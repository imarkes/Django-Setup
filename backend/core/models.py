from django.db import models


class Cliente(models.Model):
    """Tabela de Clientes. """
    nome = models.CharField(max_length=100, null=False)
    nascimento = models.DateField(null=False)
    sexo = models.CharField(max_length=2, null=False, choices=(('M', 'masculino'), ('F', 'femenino')
                                                               ))

    def __str__(self):
        return self.nome



