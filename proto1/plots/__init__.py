__author__ = 'gautam'
import importlib

from proto1 import app_settings as settings


def get_factor(factor_name):
    factor_module_name = settings.REGISTERED_PLOTS.get(factor_name)
    factor_class = None
    if factor_module_name:
        factor_parts = factor_module_name.split('.')
        module_name = '.'.join(factor_parts[:-1])  # Second to last item on the list
        class_name = factor_parts[-1]
        factor_module = importlib.import_module(module_name)
        factor_class = getattr(factor_module, class_name)
    return factor_class
