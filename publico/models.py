from django.db import models

class Publico(models.Model):
    nome = models.CharField('Nome:', max_length=30)
    mae = models.CharField('Mãe:', max_length=30, null=True, blank=True)
    logradouro = models.CharField('Nome da rua:', max_length=60)
    numero = models.CharField('Número:', max_length=6)
    complemento = models.CharField('Complemento:', max_length=30, null=True, blank=True)
    bairro = models.CharField('Bairro:', max_length=30, null=True, blank=True)
    telefone1 = models.CharField('Telefone 1:', max_length=16, blank=True, null=True)
    telefone2 = models.CharField('Telefone 2:', max_length=16, blank=True, null=True)
    email = models.CharField('Email:', max_length=30, blank=True, null=True)
    lotacao = models.CharField("Lotado em:", choices=[("BM","Bombeiro Miliar"),("PM","Policia Miliar"), ("OUTROS","Outros")], max_length=2)
    matricula = models.CharField("Nr policia/Bombeiro", max_length=9)
    data_nascimento = models.DateField("Data nascimento:")
    observacoes = models.TextField("Observações:", max_length=1600, blank=True)

    def __str__(self):
        return self.nome

class Dependentes(models.Model):
    responsavel = models.ForeignKey("Publico", on_delete=models.CASCADE)
    nome = models.CharField('Nome dependente:', max_length=30)
    parentesco = models.CharField('Relacionamento com titular:', choices=[("FILHO(A)","Filho(a)"),
                                                                          ("ENTEADO(A)","Enteado(a)"),
                                                                          ("CONJUGE", "Conjuge"),
                                                                          ("OUTROS","Outros")], max_length=10)
    data_nascimento = models.DateField("Data nascimento:")
    observacoes = models.TextField("Observações:", max_length=1600, blank=True)

    def __str__(self):
        return "{} - {} - {}".format(self.nome.upper(), self.data_nascimento, self.parentesco)

class Locacao(models.Model):
    material = models.ForeignKey('material.Material',  on_delete=models.CASCADE)
    locador = models.ForeignKey("Publico",  on_delete=models.CASCADE)
    data_locado = models.DateField()
    data_devolucao = models.DateField()
    observacao = models.TextField("Observações:", max_length=800, blank=True)

    def __str__(self):
        return "{} de {} até {}".format(self.material, self.data_locado, self.data_devolucao)
