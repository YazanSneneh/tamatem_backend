from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class UserModel(AbstractUser):
    """
        A custom user model that extends the AbstractUser model,
        so I can use my use case user model.

        Args:
            None

        Returns:
            None

        Examples:
            This model can be used to create custom user models in Django.
    """
    pass