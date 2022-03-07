from django.db import models


class Cliente(models.Model):
    """Tabela de Clientes. """
    nome = models.CharField(max_length=100, null=False)
    nascimento = models.DateField(null=False)
    sexo = models.CharField(max_length=2, null=False, choices=(('M', 'masculino'), ('F', 'femenino')
                                                               ))

    def __str__(self):
        return self.nome


class Endereco(models.Model):
    """ Tabela de Endereços."""
    rua = models.CharField(max_length=(70), null=False)
    numero = models.IntegerField(null=False)
    complemento = models.CharField(max_length=100, null=False)
    cidade = models.CharField(max_length=100, null=False)
    cep = models.CharField(max_length=8, null=False)
    bairro = models.CharField(max_length=100, null=False)
    uf = models.CharField(max_length=2, null=False)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return self.rua
