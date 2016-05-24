import json
from collections import OrderedDict

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render

from v2 import app_settings
from v2.plots import get_plot_class_v2

# Create your views here.
from v2.scenario import Scenario
from v2.util import serialize_scenario


@login_required
def home(request):
    return render(request, 'v2/home.html', {
        'ALLOWED_STATES': app_settings.ALLOWED_STATES,
        'ALLOWED_YEARS': map(lambda year: {'year': year, 'label': '%d - %d' % (year - 1, year)}, settings.ALLOWED_YEARS)
    })


def bulk_api(request):
    pass


@login_required
def api_html_view(request, results):
    plots = {}
    mfi = results['scenario']['median_family_income'][0]['income']
    for key, value in results['plots'].iteritems():
        if value.get('data'):
            plots[key] = value['data']
        else:
            results['scenario'][key] = value
    return render(request, 'v2/debug.html', {
        'plots': plots,
        'scenario': results['scenario'],
        'x_values': ("${} ( {} )".format(percent_mfi * mfi / 100, percent_mfi) for percent_mfi in xrange(1, 201))
    })


@login_required
def api_plot(request):
    results = {
        'plots': OrderedDict()
    }
    request_data = request.GET if request.method == 'GET' else request.POST
    plots = json.loads(request_data.get('plots', '[]'))
    scenario_dict = json.loads(request_data.get('scenario', '{}'))
    scenario = Scenario(scenario_dict)
    for plot_name in plots:
        plot_class = get_plot_class_v2(plot_name, module=scenario.get_state())
        if plot_class:
            plot = plot_class(scenario)
            results['plots'][plot_name] = plot.execute()
    results['scenario'] = serialize_scenario(scenario)

    if request.GET.get('debug_view', 'false').lower() == 'true':
        return api_html_view(request, results)
    return JsonResponse(results)


@login_required
def list_plots(request):
    return JsonResponse({
        'plots': app_settings.REGISTERED_PLOTS.keys()
    })
