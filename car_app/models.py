from django.db import models

class Car(models.Model):
    name = models.CharField(max_length=120)
    model = models.CharField(max_length=120)
    year = models.IntegerField()
    transmission = models.SmallIntegerField(choices=[(1, 'Mechanics'), (2, 'Automatic'), (3, 'Robot')])
    color = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photo', blank=True, null=True)

    def __str__(self):
        return self.name