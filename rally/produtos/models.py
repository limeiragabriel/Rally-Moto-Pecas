from django.contrib.auth.models import Permission, User
from django.db import models
from django.core.urlresolvers import reverse
#teste
import hashlib
#hash = sha_constructor(settings.SECRET_KEY + unicode(request.user) + datetime.now().strftime("%d/%m/%Y %H:%M:%S %f"))
#token = hash.hexdigest()
# teste

class Produto(models.Model):
    user = models.ForeignKey(User, default=1)
    nome = models.CharField(max_length=250)
    valor = models.DecimalField(max_digits=20, decimal_places=2)
    estoque = models.IntegerField()
    imagem = models.FileField()

    def get_absolute_url(self):
        return reverse('produtos:detail', kwargs={'pk':self.pk})

    def __str__(self):
        return self.nome + ' - ' + str(self.estoque)