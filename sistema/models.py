from django.db import models

STATUS_CHOICES = (('A', 'Ativo'), ('I', 'Inativo'))

class Cliente(models.Model):
    nome_cliente = models.CharField(max_length=200)
    cpf_cliente = models.CharField(max_length=20)
    telefone_cliente = models.CharField(max_length=14)
    email_cliente = models.CharField(max_length=20)
    rg_cliente = models.CharField(max_length=50)
    cnpj_cliente = models.CharField(max_length=50)
    cnh_cliente = models.CharField(max_length=100)
    validade_cnh = models.CharField(max_length=50)
    endereco_cliente = models.ForeignKey('Endereco', on_delete=models.CASCADE)
    status = models.CharField(max_length=6, choices=STATUS_CHOICES)
    criado_em = models.DateTimeField(auto_now=True)
    modificado_em = models.DateTimeField(auto_now_add=True)


class Endereco(models.Model):
    rua = models.CharField('Rua', max_length=200)
    numero = models.IntegerField()
    complemento = models.CharField(max_length=200)
    cep = models.CharField(max_length=10)
    bairro = models.CharField(max_length=200)
    cidade = models.CharField(max_length=200)

    def __str__(self):
        return self.rua

class Locacao(models.Model):
    dt_hora_locacao = models.CharField(max_length=50)
    dt_hora_devolucao = models.CharField(max_length=50)
    quilometragem = models.FloatField()
    valor_locacao = models.DecimalField(max_digits=6, decimal_places=2)
    # usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE)
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    automovel = models.ForeignKey('Automovel', on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now=True)
    modificacado_em = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)

    def __str__(self):
        return self.cliente


class Automovel(models.Model):
    placa_automovel = models.CharField(max_length=15)
    cor_automovel = models.CharField(max_length=20)
    nro_portas_automovel = models.IntegerField()
    tipo_combustivel_automovel = models.CharField(max_length=20)
    quilometragem_automovel = models.FloatField()
    chassi_automovel = models.IntegerField()
    valor_locacao = models.DecimalField(max_digits=6, decimal_places=2)
    modelo_automovel = models.ForeignKey('Modelo', on_delete=models.CASCADE)
    ano_automovel = models.IntegerField()
    marca_automovel = models.CharField(max_length=50)
    categoria_automovel = models.ForeignKey('Categoria', on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now=True)
    modificacado_em = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)


    def __str__(self):
        return self.modelo_automovel


class Marca(models.Model):
    descricao_marca = models.CharField(max_length=200)

    def __str__(self):
        return self.descricao_marca


class Modelo(models.Model):
    modelo = models.CharField(max_length=200)

    def __str__(self):
        return self.modelo


class Categoria(models.Model):
    nome_categoria = models.CharField(max_length=200)
    valor_diario = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.nome_categoria
