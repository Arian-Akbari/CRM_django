from django.db import models
from django.contrib.auth.models import AbstractUser


# better to create your own user b for bigger projects it becomes a big problem


# this thing is editable and we can add anything we want to it

class User(AbstractUser):
    pass


class Agent(models.Model):
    user = models.OneToOneField("User", on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email


class lead(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField(default=0)
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)

# SOURCE_CHOICE = (
#     ('Youtube', 'Youtube'),
#     ('Google', 'Google'),
#     ('Newsletter', 'Newsletter'),
# )
# phoned = models.BooleanField(default=False)
# source = models.CharField(choices=SOURCE_CHOICE, max_length=100)
#
# profile_picture = models.ImageField(blank=True, null=True)
# special_files = models.FileField(blank=True, null=True)
