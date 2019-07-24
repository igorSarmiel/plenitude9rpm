from django.db import models


TIPOS_CHOICE = [('ANDADOR','Andador'),('MULETA','Muleta'),('CADEIRA_RODAS','Cadeira de Rodas'),
                ('CADEIRA_BANHO','Cadeira de banho'), ('CAMA','Cama'),('COLCHAO','Colchão'),
                ('TIPOIA','Tipoia'),('COLAR_CERVICAL','Colar Cervical'),('BOTA_ORTOPEDICA','Bota_ortopédica'),
                ('OUTROS','Outros'), ]

class Material(models.Model):
    tipo = models.CharField('Tipo do material:',max_length=30, choices=TIPOS_CHOICE)
    caracteristicas = models.CharField('Caracteristica do material:', max_length=60)
    nr = models.CharField('NR do material:', max_length=30, null=True, blank=True)
    observacoes = models.CharField('Observações do material:', max_length=60, null=True, blank=True)
    locado = models.BooleanField('Locado:', default=False)

    def __str__(self):
        return "{} - {} - {}".format(self.nr, self.tipo, self.caracteristicas,)
