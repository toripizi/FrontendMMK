from django.db import models


class LogMessage(models.Model):
    # id = models.BigAutoField(primary_key=True)
    value = models.JSONField()
