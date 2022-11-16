from django.db import models

# Create your models here.


class Rating(models.Model):
    SCORE_CHOICES = [
        (1, 'really_bad'),
        (2, 'bad'),
        (3, 'regular'),
        (4, 'good'),
        (5, 'very_good'),
    ]
    score = models.PositiveSmallIntegerField(
        verbose_name='Nota de 1 a 5', choices=SCORE_CHOICES, null=False)
    message = models.CharField(
        verbose_name='Comentário', max_length=255, null=True)
    created_at = models.DateTimeField(
        verbose_name='Data de entrada', auto_now_add=True)

    class Meta:
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'

    def __str__(self) -> str:
        return f'{self.id}: Nota {self.score}, "{self.message}"'


class UserRatings(models.Model):
    rating = models.OneToOneField('review.Rating',
                                  verbose_name='Avaliação', null=False, on_delete=models.PROTECT)
    sender = models.ForeignKey(
        'authentication.User', verbose_name='Avaliador', on_delete=models.PROTECT, related_name='sender')
    target = models.ForeignKey(
        'authentication.User', verbose_name='Avaliado', on_delete=models.CASCADE, related_name='target')

    class Meta:
        verbose_name = 'Avaliação de Usuário'
        verbose_name_plural = 'Avaliações de Usuários'

    def __str__(self) -> str:
        return f'{self.id}: {self.sender} to {self.target} - {self.rating}'


class PlaceRatings(models.Model):
    rating = models.OneToOneField('review.Rating',
                                  verbose_name='Avaliação', null=False, on_delete=models.PROTECT)
    user = models.ForeignKey('authentication.User',
                             verbose_name='Cliente', null=False, on_delete=models.CASCADE)
    place = models.ForeignKey('places.PlaceAds',
                              verbose_name='Lugar', null=False, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Avaliação de Lugar'
        verbose_name_plural = 'Avaliações de Lugares'

    def __str__(self) -> str:
        return f'{self.id}: {self.user}, {self.place} - {self.rating}'
