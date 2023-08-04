from django.db import models

# Create your models here.
# models.py

class RabbitManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().using('rabbits')


class Rabbit(models.Model):
    rabbit_id = models.IntegerField(primary_key=True)
    rabbit_name = models.TextField()
    rabbit_temp = models.FloatField()
    rabbit_temp_med = models.FloatField()
    rabbit_pulse = models.FloatField()
    rabbit_pulse_med = models.FloatField()

    class Meta:
        db_table = 'rabbits_group_1'

    objects = RabbitManager()

    def __str__(self):
        return self.rabbit_name

