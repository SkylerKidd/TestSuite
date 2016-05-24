import hashlib
import json

from django.conf import settings
from django.core.cache import cache
from django.core.serializers.json import DjangoJSONEncoder
from django.db import models
from django.forms.models import model_to_dict


class ScenarioJSONEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, models.Model):
            return json.dumps(model_to_dict(obj))
        return super(ScenarioJSONEncoder, self).default(obj)


def serialize_scenario(scenario):
    for key, val in scenario.iteritems():
        updated = []
        if type(val) == list:
            if len(val) > 0 and isinstance(val[0], models.Model):
                for instance in val:
                    updated.append(model_to_dict(instance))
                scenario[key] = updated
    return scenario


def generate_cache_key(function_name, **kwargs):
    kwargs['function_name'] = function_name
    return hashlib.md5(json.dumps(kwargs)).hexdigest()


def method_cache(func):
    def func_wrapper(*args, **kwargs):
        cache_key = hashlib.md5(json.dumps({
            'args': args,
            'kwargs': kwargs,
            'function_name': func.__name__
        })).hexdigest()
        cache_value = cache.get(cache_key)
        if not cache_value:
            cache_value = func(*args, **kwargs)
            cache.set(cache_key, cache_value, settings.CACHE_LENGTH)
        return cache_value

    return func_wrapper
