from django.db import models

# Create your models here.

class Car(models.Model):

    name = models.CharField('Car name', max_length=50)
    img = models.ImageField('Car image', upload_to='car_images')
    price = models.PositiveBigIntegerField('Car price')

    def __str__(self):
        return self.name


class About(models.Model):

    text = models.TextField('About page content')


class Contact(models.Model):

    user_name = models.CharField('User name', max_length=80)
    user_email = models.EmailField('User email')
    user_review = models.TextField('User review')

    def __str__(self):
        return self.user_name