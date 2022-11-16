from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.


class EventOrder(models.Model):
    STATUS = [
        (1, "open"),
        (2, "accepted"),
        (3, "refused"),
        (4, "canceled"),
    ]
    user = models.ForeignKey(
        'authentication.User', verbose_name="Cliente", on_delete=models.CASCADE)
    place_ads = models.ForeignKey('places.PlaceAds', verbose_name="Anúncio",
                                  on_delete=models.CASCADE, null=False, blank=False)

    dates_selected = models.ManyToManyField('places.Date')
    title = models.CharField(
        verbose_name='Título do evento', max_length=45, null=False)
    description = models.CharField(
        verbose_name='Descrição do evento', max_length=255, null=False)
    price = models.DecimalField(
        verbose_name="Preço", max_digits=10, decimal_places=2, null=False)
    status = models.PositiveSmallIntegerField(
        verbose_name='Status', choices=STATUS, default=1)
    created_at = models.DateTimeField(
        verbose_name="Data de criação", auto_now_add=True)

    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"

    def __str__(self):
        return f'{self.id}: {self.passenger} - {self.created_at}'


class Cancellation(models.Model):
    event_order = models.ForeignKey(
        'events.EventOrder', verbose_name='Evento', on_delete=models.CASCADE, null=False, blank=False)
    justification = models.CharField(
        verbose_name='Justificativa',
        max_length=255,
        null=False,
    )
    created_at = models.DateTimeField(
        verbose_name="Data de criação", auto_now_add=True)

    class Meta:
        verbose_name = "Cancelamento"
        verbose_name_plural = "Cancelamentos"

    def __str__(self):
        return f'{self.id} in {self.order}: "{self.justification}"'


class History(models.Model):
    user = models.ForeignKey('authentication.User',
                             verbose_name='Cliente', null=False, on_delete=models.PROTECT)
    event_order = models.ForeignKey(
        'events.EventOrder', verbose_name='Evento', null=False, on_delete=CASCADE)
    description = models.CharField(
        verbose_name='Descrição do evento', max_length=255, null=False)
    created_at = models.DateTimeField(
        verbose_name="Data de criação", auto_now_add=True)

    class Meta:
        verbose_name = "Histórico de Evento"
        verbose_name_plural = "Históricos de Eventos"

    def __str__(self):
        return f'{self.id}: {self.event_order} - {self.created_at}'
