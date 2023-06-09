from django.db import models


class User(models.Model):
    """用户表"""

    name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name
