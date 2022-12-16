from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

# Create your models nota.

class UserManager(BaseUserManager):
    def _create_user(self, usuario, email, nombre,apellido, password):
        user = self.model(
            usuario = usuario,
            email = email,
            nombre = nombre,
            apellido = apellido,
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, usuario, email, nombre,apellido, password):
        user = self._create_user(usuario, email, nombre,apellido, password)
        user.is_staff = True
        user.is_superuser = True
        return user

class User(AbstractBaseUser, PermissionsMixin):
    usuario = models.CharField(max_length = 255, unique = True)
    email = models.EmailField('Correo Electrónico',max_length = 255, unique = True,)
    nombre = models.CharField('Nombres', max_length = 255, blank = True, null = True)
    apellido = models.CharField('Apellido', max_length = 255, blank = True, null = True)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
    objects = UserManager()

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    USERNAME_FIELD = 'usuario'
    REQUIRED_FIELDS = ['email','nombre','apellido']

    def __str__(self):
        return f'{self.nombre} {self.apellido}'