import itertools

import django
from tablib import Dataset

from ipeds.models import AppropriationsModel

CSV_PATH = '/tmp/mergedipedswithreadableheaders/Appropriations_merged_header_names.csv'
MODEL = AppropriationsModel

ERROR_COUNT = 0
ROW_COUNT = 0


def integer_or_nothing(value):
    global ERROR_COUNT
    try:
        return int(value)
    except (ValueError, TypeError) as e:
        ERROR_COUNT += 1
        return 0


def row_mapper(row):
    data_dict = {k: integer_or_nothing(row.get(k)) for k in
                 filter(lambda name: name != 'id', MODEL._meta.get_all_field_names())}
    return data_dict


def validation_filter(data_dict):
    if not data_dict['institution_id']:
        return False
    if not data_dict['fiscal_year']:
        return False
    if not data_dict['state_appropriation'] and not data_dict['local_appropriation']:
        return False
    return True


def model_mapper(data_dict):
    global ROW_COUNT
    ROW_COUNT += 1
    return MODEL(**data_dict)


def main():
    global ERROR_COUNT
    django.setup()
    csv = Dataset().load(open(CSV_PATH).read())

    row_mapped = itertools.imap(row_mapper, csv.dict)
    validated = itertools.ifilter(validation_filter, row_mapped)
    models = itertools.imap(model_mapper, validated)
    MODEL.objects.bulk_create(models)
    print "{} rows processed with {} errors".format(ROW_COUNT, ERROR_COUNT)


if __name__ == '__main__':
    main()
