from django.db import models

class Currency(models.Model):
    id = models.CharField(primary_key=True, max_length=3)
    label = models.CharField(max_length=256)

    @classmethod
    def new(cls, id, label):
        inst = cls()
        inst.id = id
        inst.label = label
        return inst
