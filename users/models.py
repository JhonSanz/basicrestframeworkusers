from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):

    profession = CharField(_("Profession of User"), blank=False, max_length=255)
