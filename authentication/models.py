from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)

from .signals import password_reset_token_created

# Register your models here.


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, email, password, **extra_fields):
        if not username:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(
            username=username,
            email=email,
            password=password,
            ** extra_fields,
        )
        user.save()
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, email, password, **extra_fields)


class User(PermissionsMixin, AbstractBaseUser):
    STATUS = [
        (1, "active"),
        (2, "inactive"),
        (3, "blocked"),
    ]
    asset = models.ForeignKey('asset.Asset', verbose_name='Foto de Perfil',
                              on_delete=models.SET_NULL, null=True, blank=True)
    address = models.OneToOneField(
        'places.Address',
        verbose_name="Endereço",
        null=True,
        on_delete=models.SET_NULL,
    )
    cpf_cnpj = models.CharField(
        verbose_name='CPF/CNPJ', max_length=14, null=False, blank=False, unique=True)
    email = models.EmailField(verbose_name='E-mail', max_length=60,
                              unique=True, null=False, blank=False)
    username = models.CharField(
        verbose_name='Nome de Usuário', max_length=30, unique=True, null=False, blank=False)
    phone = models.CharField(verbose_name="Telefone", max_length=30,
                             blank=False, null=False, unique=True)
    whatsapp = models.CharField(verbose_name="WhatsApp", max_length=30,
                                blank=False, null=False, unique=True)
    first_name = models.CharField(
        verbose_name='Nome', max_length=30, null=False, blank=False)
    last_name = models.CharField(
        verbose_name='Sobrenome', max_length=60, null=False, blank=False)
    status = models.PositiveSmallIntegerField(choices=STATUS, default=1)
    password = models.CharField(
        verbose_name='Senha', max_length=128, null=False, blank=False)
    created_at = models.DateTimeField(
        verbose_name='Data de Entrada', auto_now_add=True)

    is_staff = models.BooleanField('Equipe', default=False)  # django user
    is_active = models.BooleanField('Ativo', default=True)  # django user

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'phone']

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    def __str__(self):
        return self.email

    # TODO rating property

    def save(self, *args, **kwargs):
        self.first_name = self.first_name.upper()
        self.last_name = self.last_name.upper()

        if not self.password.startswith('pbkdf2_sha256'):
            self.password = make_password(self.password)

        super(User, self).save(*args, **kwargs)
