from django.db import models

import itertools
from typing import Dict

# Create your models here.


class RandomQuestion(models.Model):
    question_id = models.IntegerField(unique=True, blank=False)
    question = models.CharField(max_length=350, blank=False)
    created_at = models.DateTimeField(db_comment="date from jservice.io API")
    answer = models.CharField(max_length=350, blank=False)

    def to_dict(instance) -> Dict:
        opts = instance._meta
        data = {}
        for f in itertools.chain(opts.concrete_fields, opts.private_fields):
            data[f.name] = f.value_from_object(instance)

        return data


