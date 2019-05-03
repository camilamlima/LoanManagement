from django.db import models


class Payload(models.Model):
    loan_id = models.AutoField(primary_key=True)
    amount = models.FloatField()
    term = models.IntegerField()
    rate = models.FloatField()
    date = models.DateField()

    def __str__(self):
        return f'Payload Id: {self.loan_id}'
