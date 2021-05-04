from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics') # Upload to profile_pics folder inside media folder in the root.
    bio = models.TextField(default='Your Bio here....', max_length=100, blank=True)
    THEME_CHOICES = (
        ('Dark', 'Dark'),
        ('Light', 'Light')
    )
    theme = models.CharField(max_length=10, choices=THEME_CHOICES, blank=True)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'      # Dunder method to return a proper name to the profile in the admin's database.

    def save(self, *args, **kwargs):                # Method to reopen the uploaded profile pic, resize it and then save it again.
        super(Profile, self).save(*args, **kwargs)

        # img = Image.open(self.image.path)

        # if img.height > 300 or img.width > 300:
        #     output_size = (300, 300)
        #     img.thumbnail(output_size)
        #     img.save(self.image.path)
