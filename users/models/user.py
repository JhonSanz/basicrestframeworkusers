""" User model definition """

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """ Extended User definition """

    profession = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """ Sets human readable name """
        verbose_name = "Extended User"

    def get_user_name(self):
        """ Format user name
        
        Returns:
            (str): User first name with last name
        """
        return "{} {}".format(self.first_name, self.last_name)

    def __str__(self):
        return self.get_user_name()
