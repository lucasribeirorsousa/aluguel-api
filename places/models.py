from django.db import models


# Create your models here.

class Address(models.Model):
    map_string = models.CharField(verbose_name="Logradouro", max_length=200, null=False, blank=False)
    reference = models.CharField(verbose_name="Ponto de Referência", max_length=60, null=False, blank=False)
    latitude = models.CharField('Latitude', max_length=50, null=True)
    longitude = models.CharField('Longitude', max_length=50, null=True)

    class Meta:
        verbose_name = "Endereço"
        verbose_name_plural = "Endereços"

    def __str__(self):
        return f'{self.id}: {self.map_string} - {self.coordinates}'


class Date(models.Model):
    date = models.DateField(verbose_name="Data", null=False)

    class Meta:
        verbose_name = "Data"
        verbose_name_plural = "Datas"

    def __str__(self):
        return f'{self.id}: {self.date}'


class Days(models.Model):
    DAYS = [
        (0, "sunday"),
        (1, "monday"),
        (2, "tuesday"),
        (3, "wednesday"),
        (4, "thursday"),
        (5, "friday"),
        (6, "saturday"),
    ]
    day = models.PositiveSmallIntegerField(
        verbose_name="Dia da semana",
        null=False,
        choices=DAYS,
        unique=True,
    )

    class Meta:
        verbose_name = "Dia da Semana"
        verbose_name_plural = "Dias da Semana"

    def __str__(self):
        return self.DAYS[self.day][1]


class DailyCost(models.Model):
    place_ads = models.ForeignKey('places.PlaceAds',
                                  verbose_name="Anúncio", null=False, on_delete=models.CASCADE)
    week_days = models.ManyToManyField('places.Days')
    price = models.DecimalField(
        verbose_name="Preço", max_digits=10, decimal_places=2, null=False)
    created_at = models.DateTimeField(
        verbose_name="Data de criação", auto_now_add=True)

    class Meta:
        verbose_name = "Diária"
        verbose_name_plural = "Diárias"

    # TODO rating property

    def __str__(self):
        return f'{self.id}: {self.place_ads} - {self.week_days}'


class PlaceAds(models.Model):
    LOCAL = [
        (1, 'Chácara'),
        (2, 'Fazenda'),
        (3, 'Galpão'),
        (4, 'Flutuante'),
    ]
    CAPACITY = [
        (1, 'Menos de 5 pessoas'),
        (2, 'Até 10 pessoas'),
        (3, 'Até 20 pessoas'),
        (4, 'Até 50 pessoas'),
        (5, 'Até 100 pessoas'),
    ]
    STATUS = [
        (1, 'open'),
        (2, 'closed'),
    ]
    user = models.ForeignKey('authentication.User',
                             verbose_name="Dono", null=False, on_delete=models.PROTECT)
    address = models.ForeignKey('places.Address',
                                verbose_name="Endereço", null=False, on_delete=models.PROTECT)
    images = models.ManyToManyField('asset.Asset')
    name = models.CharField(
        verbose_name='Nome do local', max_length=30, null=False)
    ads_description = models.CharField(
        verbose_name='Descrição do anúncio', max_length=200, null=False)
    place_description = models.CharField(
        verbose_name='Descrição do local', max_length=400, null=False)
    local_type = models.PositiveSmallIntegerField(
        verbose_name="Tipo de Local", choices=LOCAL, null=False)
    capacity = models.PositiveSmallIntegerField(
        verbose_name="Capacidade", null=False, choices=CAPACITY)
    week_days = models.ManyToManyField('places.Days')
    status = models.PositiveSmallIntegerField(
        verbose_name="Status", choices=STATUS, null=False)
    created_at = models.DateTimeField(
        verbose_name="Data de criação", auto_now_add=True)

    # TODO place score

    class Meta:
        verbose_name = "Anúncio de local"
        verbose_name_plural = "Anúncios de locais"

    def __str__(self):
        return f'{self.id}: {self.name} - {self.ads_description}'
