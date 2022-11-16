from django.db import models
from django.utils import timezone

from datetime import datetime


def validation_expires_date():
    now_plus_1_hour = int(datetime.now().strftime("%s")) + 3.6 * 1e2
    naive_datetime = datetime.fromtimestamp(now_plus_1_hour)
    aware_datetime = timezone.make_aware(naive_datetime)
    return aware_datetime


class Validation(models.Model):
    email = models.EmailField(verbose_name="Email",
                              max_length=120, null=False, blank=False)
    cpf_cnpj = models.CharField(
        verbose_name="CPF/CNPJ", max_length=11, null=False, blank=False)
    phone = models.CharField(verbose_name="Telefone",
                             max_length=12, blank=False, null=False)
    code = models.CharField(verbose_name="Código de Validação",
                            max_length=128, null=False, blank=False)
    expires_date = models.DateTimeField(
        verbose_name="Data de Validade", default=validation_expires_date)
    created_at = models.DateTimeField(
        verbose_name="Data de Criação", auto_now_add=True)

    class Meta:
        verbose_name = "Validação de Cadastro"
        verbose_name_plural = "Validações de Cadastros"

    def __str__(self):
        return f'{self.id}: {self.email} - {self.cpf_cnpj} - {self.phone}'
