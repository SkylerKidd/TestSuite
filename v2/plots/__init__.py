__author__ = 'gautam'
import importlib

from v2 import app_settings as settings


def get_plot_class(factor_name):
    factor_module_name = settings.REGISTERED_PLOTS.get(factor_name)
    factor_class = None
    if factor_module_name:
        factor_parts = factor_module_name.split('.')
        module_name = '.'.join(factor_parts[:-1])  # Second to last item on the list
        class_name = factor_parts[-1]
        factor_module = importlib.import_module(module_name)
        factor_class = getattr(factor_module, class_name)
    return factor_class


def security_check(plot_name, module):
    if module not in settings.PlotClassMapping.MODULES and module != settings.PlotClassMapping.DEFAULT_MODULE:
        return False
    if plot_name not in settings.PlotClassMapping.PLOTS:
        return False
    return True


def get_plot_class_v2(plot_name, module=settings.PlotClassMapping.DEFAULT_MODULE):
    if not security_check(plot_name, module):
        return None
    plot_module = importlib.import_module(name=settings.PlotClassMapping.MODULES.get(module),
                                          package=settings.PlotClassMapping.PACKAGE)
    plot_class = getattr(plot_module, settings.PlotClassMapping.PLOTS[plot_name])
    return plot_class
