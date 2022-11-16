from django.db import models
from random import getrandbits
from .utils import resize_and_crop_file


def upload_directory_path(instance, filename):
    HASH = getrandbits(100)
    return f'{HASH}-{filename}'


class Asset(models.Model):
    FILE_CHOICES = (
        (1, 'image'),
        (2, 'banner'),
        (3, 'other'),
    )

    file_type = models.PositiveSmallIntegerField(
        'Tipo de Arquivo',
        choices=FILE_CHOICES,
        default=1,
        null=False,
    )
    file_high = models.FileField(
        'Arquivo (high)',
        upload_to=upload_directory_path,
        blank=False,
        null=False,
    )
    file_medium = models.FileField(
        'Arquivo (medium)',
        upload_to=upload_directory_path,
        null=True,
    )
    file_low = models.FileField(
        'Arquivo (low)',
        upload_to=upload_directory_path,
        null=True,
    )
    uploaded_at = models.DateTimeField('Data de Entrada', auto_now_add=True)

    class Meta:
        verbose_name = "Arquivo"
        verbose_name_plural = "Arquivos"

    def __str__(self):
        return f'{self.id}: {self.file_high}'

    def save(self, *args, **kwargs):
        if self.file_type == 1:
            self.file_high = resize_and_crop_file(
                self.file_high, multiplier=1,
            )
            self.file_medium = resize_and_crop_file(
                self.file_high, multiplier=2,
            )
            self.file_low = resize_and_crop_file(
                self.file_high, multiplier=3,
            )
        else:
            self.file_medium = None
            self.file_low = None

        super(Asset, self).save(*args, **kwargs)


class Banner(models.Model):
    asset = models.OneToOneField(
        "asset.Asset", null=False, on_delete=models.CASCADE,
    )
    spot = models.ForeignKey(
        "asset.Spot", null=False, on_delete=models.CASCADE,
    )
    hyperlink = models.CharField(
        verbose_name='Hyperlink', max_length=255, null=False, blank=False
    )
    description = models.CharField(
        verbose_name='Descrição', max_length=255, null=False, blank=False
    )
    expires = models.DateTimeField(
        verbose_name='Data e Hora de expiração', null=False, auto_now_add=False
    )

    class Meta:
        verbose_name = 'Banner'
        verbose_name_plural = 'Banners'

    def __str__(self):
        return f'Hyperlink {self.id}: {self.hyperlink}'


class Spot(models.Model):
    SPOT_POSITIONS = (
        ('principal', 'principal_spot'),
    )
    description = models.CharField(
        verbose_name='Descrição', max_length=255, null=False, blank=False
    )
    location = models.CharField(
        verbose_name='Localização do Spot', choices=SPOT_POSITIONS,
        max_length=20, null=False, blank=False, unique=True,
    )
    created_at = models.DateTimeField(
        verbose_name='Data de Criação', auto_now_add=True
    )

    def __str__(self):
        return f'Spot {self.id}: {self.description} ({self.location})'
