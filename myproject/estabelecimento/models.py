from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User

# Importe o modelo Endereco diretamente, se necessário
from Enderecos.models import Endereco

class Estabelecimento(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    telefone = models.BigIntegerField()
    descricao = models.TextField()
    foto_local = models.ImageField(upload_to='estabelecimentos/fotos/', null=True, blank=True)
    media_avaliacao = models.FloatField(default=0.0)
    lat = models.CharField(max_length=255)
    lng = models.CharField(max_length=255)

    # Foreign Keys (FK)
    proprietario = models.ForeignKey(User, on_delete=models.CASCADE)
    # Atualize aqui para referenciar o modelo Endereco
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)
    categoria = models.ForeignKey('categorias.Categoria', on_delete=models.CASCADE)

    def __str__(self):
        return f"Estabelecimento {self.nome} - {self.descricao[:50]}"

    class Meta:
        db_table = 'estabelecimento'

    # Método para criar um novo estabelecimento
    @classmethod
    def criar_estabelecimento(cls, nome, telefone, descricao, proprietario, endereco, categoria, foto_local=None, media_avaliacao=0.0):
        estabelecimento = cls(
            nome=nome,
            telefone=telefone,
            descricao=descricao,
            proprietario=proprietario,
            endereco=endereco,
            categoria=categoria,
            foto_local=foto_local,
            media_avaliacao=media_avaliacao
        )
        estabelecimento.save()
        return estabelecimento

    # Método para buscar um estabelecimento por ID
    @classmethod
    def buscar_estabelecimento_por_id(cls, id):
        try:
            return cls.objects.get(id=id)
        except ObjectDoesNotExist:
            return None

    # Método para buscar todos os estabelecimentos
    @classmethod
    def buscar_todos_estabelecimentos(cls):
        return cls.objects.all()

    # Método para atualizar um estabelecimento existente
    def atualizar_estabelecimento(self, nome=None, telefone=None, descricao=None, foto_local=None, media_avaliacao=None, endereco=None, categoria=None):
        if nome:
            self.nome = nome
        if telefone:
            self.telefone = telefone
        if descricao:
            self.descricao = descricao
        if foto_local:
            self.foto_local = foto_local
        if media_avaliacao is not None:
            self.media_avaliacao = media_avaliacao
        if endereco:
            self.endereco = endereco
        if categoria:
            self.categoria = categoria
        self.save()
        return self

    # Método para deletar um estabelecimento
    @classmethod
    def deletar_estabelecimento(cls, id):
        try:
            estabelecimento = cls.objects.get(id=id)
            estabelecimento.delete()
            return True
        except ObjectDoesNotExist:
            return False
