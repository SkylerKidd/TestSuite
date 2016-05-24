import hashlib
import json

import constance
from django.conf import settings
from django.core.cache import cache
from django.db.models import F

from v2 import constants
from v2.models import MinimumWageModel, InstitutionModel
from v2.util import method_cache


def _find_min_wage(state, calendar_year):
    count = MinimumWageModel.objects.filter(calendar_year=calendar_year, state=state).count()
    if count > 0:
        min_wage = MinimumWageModel.objects.get(calendar_year=calendar_year, state=state).minimum_wage
    else:
        min_wage_model = MinimumWageModel.objects.filter(calendar_year__lt=calendar_year,
                                                         state=state).order_by(F(constants.CALENDAR_YEAR).desc())
        min_wage = min_wage_model.first().minimum_wage
    return min_wage


def fetch_min_wage(state, calendar_year):
    cache_key = hashlib.md5(json.dumps({
        constants.CALENDAR_YEAR: calendar_year,
        constants.STATE: state,
        'computation_name': 'minimum_wage'
    })).hexdigest()
    min_wage = cache.get(cache_key)
    if not min_wage:
        min_wage = _find_min_wage(state, calendar_year)
        cache.set(cache_key, min_wage, settings.CACHE_LENGTH)
    return min_wage


def apply_filters(filters, data):
    result = data
    for f in filters:
        result = filter(f, result)
    return result


@method_cache
def compute_nominal_time_to_graduate(institution_type):
    institutions = InstitutionModel.objects.filter(institution_type=institution_type)
    nominal_time_to_graduate = sum(i.nominal_time_to_graduate for i in institutions) / len(institutions)
    return nominal_time_to_graduate


def compute_time_to_graduate(scenario):
    ui_nominal_time_to_graduate = float(scenario.get(constants.NOMINAL_TIME_TO_GRADUATE, 0))
    ui_time_to_graduate = float(scenario.get(constants.TIME_TO_GRADUATE, 1))
    institution_type = scenario.get(constants.INSTITUTION_TYPE)
    nominal_time_to_graduate = compute_nominal_time_to_graduate(institution_type=institution_type)

    if ui_nominal_time_to_graduate:
        ui_difference = round(ui_time_to_graduate - ui_nominal_time_to_graduate, 2)
        time_to_graduate = round(nominal_time_to_graduate + ui_difference, 2)
        if time_to_graduate < constance.config.MIN_TIME_TO_GRADUATE:
            time_to_graduate = constance.config.MIN_TIME_TO_GRADUATE
    else:
        time_to_graduate = nominal_time_to_graduate

    scenario[constants.NOMINAL_TIME_TO_GRADUATE] = nominal_time_to_graduate
    scenario[constants.TIME_TO_GRADUATE] = time_to_graduate
    return time_to_graduate


def average(iterable):
    total = 0
    count = 0
    for i in iterable:
        total += i
        count += 1
    return total / count
