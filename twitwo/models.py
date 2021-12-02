from django.db import models

class Twit(models.Model):
    text = models.CharField(max_length=300)
    url = models.URLField(max_length=200, null=True)
    twit_id = models.CharField(max_length=100)

    def __str__(self):
        return self.text

    class Meta:
        db_table = 'twits'
