from django.contrib.auth.models import Permission, User
from django.db import models
from datetime import datetime

class Case(models.Model):
    type_choices = (
    	('memory', 'memory'),
    	('disk', 'disk'),
    	('network', 'network'),
    )

   # c_id = models.IntegerField(primary_key=True)
    c_name = models.CharField(max_length=250, unique=True, default='')
    c_type = models.CharField(
    	max_length=250,
    	choices=type_choices,
    	default='memory',
    )
    c_date_created = models.DateTimeField(default=datetime.now, blank=True)
    c_status = models.BooleanField(default=False)
    c_file = models.FileField(upload_to='uploads/')
    c_fingerprint = models.CharField(max_length=250, default='', unique=True)
    c_owner = models.ForeignKey(User, on_delete='')
    c_unsupported = models.BooleanField(default=False)

    def __str__(self):
        return self.c_name
