from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# from linkcut.models import CutLink

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField(default='default.jpg', upload_to='user_images')
    slug = models.SlugField(default="")
    long_link = models.CharField(max_length=255, default="")
    descriptions = models.CharField(max_length=100, default="")

    def __str__(self):
        return f'ССылки пользователя {self.user}'

    def save(self, *args, **kwargs):
        super().save()

